#!/usr/bin/env python3
import os

from crewai import Crew
from dotenv import load_dotenv
from uagents_adapter import CrewaiRegisterTool

from job_search_agents import JobSearchAgents
from job_search_tasks import JobSearchTasks


class JobSearchCrew:
    """CrewAI crew for automated job searching and matching."""
    
    def __init__(self, job_title, location, experience_level, skills, career_goals="", preferred_industry="", salary_range="", user_preferences=""):
        self.job_title = job_title
        self.location = location
        self.experience_level = experience_level
        self.skills = skills
        self.career_goals = career_goals
        self.preferred_industry = preferred_industry
        self.salary_range = salary_range
        self.user_preferences = user_preferences

    def run(self):
        """Execute the job search workflow."""
        agents = JobSearchAgents()
        tasks = JobSearchTasks()

        # Create agents
        job_market_researcher = agents.job_market_researcher()
        skills_analyzer = agents.skills_analyzer_agent()
        opportunity_curator = agents.opportunity_curator()

        # Create tasks
        market_research_task = tasks.job_market_research_task(
            job_market_researcher,
            self.job_title,
            self.location,
            self.experience_level,
            self.skills
        )
        
        skills_matching_task = tasks.skills_matching_task(
            skills_analyzer,
            self.skills,
            self.experience_level,
            self.career_goals,
            self.preferred_industry
        )
        
        opportunity_curation_task = tasks.opportunity_curation_task(
            opportunity_curator,
            self.job_title,
            self.location,
            self.user_preferences,
            self.salary_range
        )

        # Set task dependencies
        skills_matching_task.context = [market_research_task]
        opportunity_curation_task.context = [market_research_task, skills_matching_task]

        # Create crew
        crew = Crew(
            agents=[job_market_researcher, skills_analyzer, opportunity_curator],
            tasks=[market_research_task, skills_matching_task, opportunity_curation_task],
            verbose=True,
        )

        result = crew.kickoff()
        return result

    def kickoff(self, inputs=None):
        """
        Compatibility method for uAgents integration.
        Accepts a dictionary of inputs and calls run() with them.
        """
        if inputs:
            self.job_title = inputs.get("job_title", self.job_title)
            self.location = inputs.get("location", self.location)
            self.experience_level = inputs.get("experience_level", self.experience_level)
            self.skills = inputs.get("skills", self.skills)
            self.career_goals = inputs.get("career_goals", self.career_goals)
            self.preferred_industry = inputs.get("preferred_industry", self.preferred_industry)
            self.salary_range = inputs.get("salary_range", self.salary_range)
            self.user_preferences = inputs.get("user_preferences", self.user_preferences)

        return self.run()


def main():
    """Main function to demonstrate Job Search Agent with CrewAI adapter."""

    # Load API key from environment
    load_dotenv()
    api_key = os.getenv("AGENTVERSE_API_KEY")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    serper_api_key = os.getenv("SERPER_API_KEY")
    
    if not api_key:
        print("Error: AGENTVERSE_API_KEY not found in environment")
        return

    if not openai_api_key:
        print("Error: OPENAI_API_KEY not found in environment")
        return
        
    if not serper_api_key:
        print("Error: SERPER_API_KEY not found in environment")
        return

    # Set API keys in environment
    os.environ["OPENAI_API_KEY"] = openai_api_key
    os.environ["SERPER_API_KEY"] = serper_api_key

    # Create an instance of JobSearchCrew with default empty values
    job_search_crew = JobSearchCrew("", "", "", "", "", "", "", "")

    # Create tool for registering the crew with Agentverse
    register_tool = CrewaiRegisterTool()

    # Define parameters schema for the job search agent
    query_params = {
        "job_title": {"type": "str", "required": True},
        "location": {"type": "str", "required": True},
        "experience_level": {"type": "str", "required": True},
        "skills": {"type": "str", "required": True},
        "career_goals": {"type": "str", "required": False},
        "preferred_industry": {"type": "str", "required": False},
        "salary_range": {"type": "str", "required": False},
        "user_preferences": {"type": "str", "required": False},
    }

    # Register the crew with parameter schema
    result = register_tool.run(
        tool_input={
            "crew_obj": job_search_crew,
            "name": "Job Search Agent",
            "port": 8001,
            "description": "A CrewAI agent that searches for job opportunities and matches them to user skills and preferences using market research, skills analysis, and opportunity curation specialists",
            "api_token": api_key,
            "mailbox": True,
            "query_params": query_params,
            "example_query": "Find software engineering jobs in San Francisco for someone with 5+ years experience, skills in Python, React, and AWS, looking for senior roles in tech companies with 120k-180k salary range.",
        }
    )

    # Get the agent address from the result
    if isinstance(result, dict) and "address" in result:
        agent_address = result["address"]
        print(f"Agent registered with address: {agent_address}")

    print(f"\nJobSearch CrewAI agent registration result: {result}")

    # Keep the program running
    try:
        while True:
            import time
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting...")


if __name__ == "__main__":
    main()