from crewai import Agent
from crewai_tools import SerperDevTool


class JobSearchAgents:
    """Class to define all agents for job searching and matching."""

    def __init__(self):
        self.search_tool = SerperDevTool()

    def job_market_researcher(self):
        """Agent responsible for researching job markets and opportunities."""
        return Agent(
            role="Job Market Research Specialist",
            goal="Search and analyze job markets to find the best opportunities matching user requirements and preferences",
            backstory="""You are an expert job market researcher with deep knowledge of employment trends, salary ranges, 
            and job availability across different industries and locations. You excel at finding hidden job opportunities 
            and understanding what employers are looking for. Your research helps job seekers find the perfect matches 
            for their skills and career goals.""",
            tools=[self.search_tool],
            verbose=True,
            allow_delegation=False,
        )

    def skills_analyzer_agent(self):
        """Agent responsible for analyzing user skills and matching them with job requirements."""
        return Agent(
            role="Skills Analysis and Matching Expert",
            goal="Analyze user skills, experience, and preferences to identify the best job matches and career opportunities",
            backstory="""You are a career counselor and skills assessment expert with over 10 years of experience in talent 
            matching and career development. You understand how to evaluate a person's skills, experience, and career goals 
            to find the most suitable job opportunities. You can identify transferable skills and suggest career paths 
            that align with personal and professional aspirations.""",
            verbose=True,
            allow_delegation=False,
        )

    def opportunity_curator(self):
        """Agent responsible for curating and presenting job opportunities."""
        return Agent(
            role="Job Opportunity Curator",
            goal="Curate and present the best job opportunities with detailed insights and application strategies",
            backstory="""You are a professional career advisor and job search strategist who specializes in helping 
            job seekers find their ideal positions. You have extensive experience in reviewing job listings, 
            understanding company cultures, and providing actionable advice for job applications. You present 
            opportunities in a clear, organized manner with strategic insights for each position.""",
            verbose=True,
            allow_delegation=False,
        )