from crewai import Task


class JobSearchTasks:
    """Class to define all tasks for job searching and matching."""

    def job_market_research_task(self, agent, job_title, location, experience_level, skills):
        """Task for researching job market and finding opportunities."""
        return Task(
            description=f"""
            Search and analyze the job market for {job_title} positions in {location} for candidates with {experience_level} experience.
            
            Your research should include:
            1. Current job openings for {job_title} in {location}
            2. Salary ranges and compensation packages
            3. Most in-demand skills for this role: {skills}
            4. Industry trends and growth opportunities
            5. Remote work availability and hybrid options
            6. Company types hiring for this position (startups, corporations, etc.)
            7. Job market competition and demand
            8. Geographic distribution of opportunities
            9. Required qualifications and certifications
            10. Career advancement paths in this field
            
            Use web search to find current job listings from major job boards like LinkedIn, Indeed, Glassdoor, and company websites.
            Focus on finding real, current opportunities that match the candidate profile.
            
            IMPORTANT: For each job opportunity found, extract and include:
            - Direct application link/URL
            - Source job board (LinkedIn, Indeed, Glassdoor, etc.)
            - Application deadline if available
            """,
            agent=agent,
            expected_output="""A comprehensive job market research report containing:
            - List of current job openings with company names, basic details, and application links
            - Direct application URLs for each job opportunity
            - Job board sources (LinkedIn, Indeed, Glassdoor, etc.)
            - Salary range analysis for the position and location
            - Skills demand analysis and market trends
            - Industry insights and growth opportunities
            - Geographic and remote work options
            - Competition level and market demand assessment""",
        )

    def skills_matching_task(self, agent, user_skills, experience_level, career_goals, preferred_industry):
        """Task for analyzing user skills and matching them with job opportunities."""
        return Task(
            description=f"""
            Analyze the user's profile and match their skills with available job opportunities.
            
            User Profile:
            - Skills: {user_skills}
            - Experience Level: {experience_level}
            - Career Goals: {career_goals}
            - Preferred Industry: {preferred_industry}
            
            Your analysis should include:
            1. Skills gap analysis compared to market requirements
            2. Transferable skills identification
            3. Recommended job titles and roles that match the profile
            4. Skills development suggestions for better job matches
            5. Alternative career paths to consider
            6. Industry-specific requirements and certifications
            7. Competitive advantage analysis
            8. Salary expectations based on skills and experience
            9. Job readiness assessment
            10. Strategic career development recommendations
            
            Provide actionable insights for improving job search success.
            """,
            agent=agent,
            expected_output="""A detailed skills analysis and matching report containing:
            - Skills assessment with strengths and gaps
            - Recommended job titles and roles
            - Skills development roadmap
            - Alternative career paths
            - Competitive positioning analysis
            - Salary expectations and market value
            - Job readiness score and improvement suggestions""",
        )

    def opportunity_curation_task(self, agent, job_title, location, user_preferences, salary_range):
        """Task for curating and presenting the best job opportunities."""
        return Task(
            description=f"""
            Curate and present the best job opportunities for {job_title} in {location} based on user preferences and requirements.
            
            User Preferences:
            - Preferred location: {location}
            - Salary range: {salary_range}
            - Additional preferences: {user_preferences}
            
            Your curation should include:
            1. Top 10 job opportunities that best match the criteria
            2. Detailed company profiles and culture insights
            3. Job descriptions with key responsibilities
            4. Direct application links and easy-apply options
            5. Application strategies for each opportunity
            6. Interview preparation tips specific to each company
            7. Networking opportunities and referral potential
            8. Company growth prospects and career advancement
            9. Work-life balance and company benefits analysis
            10. Application deadlines and urgency levels
            11. Success probability assessment for each opportunity
            
            CRITICAL: For each job opportunity, provide:
            - Direct application URL (clickable link)
            - Job board source (LinkedIn, Indeed, Glassdoor, company website)
            - Application method (direct apply, email, company portal)
            - Application deadline if available
            
            Present opportunities in order of best fit with strategic application advice.
            Format the output as a comprehensive job search guide with actionable application links.
            """,
            agent=agent,
            expected_output="""A curated job opportunities guide containing:
            - Top 10 ranked job opportunities with detailed analysis and direct application links
            - Company profiles and culture insights
            - Clickable application URLs for each position
            - Job board sources and application methods
            - Tailored application strategies for each position
            - Interview preparation tips and company-specific advice
            - Networking and referral opportunities
            - Timeline and priority recommendations
            - Success probability assessment
            - Next steps action plan for job applications
            The guide should be actionable with ready-to-use application links for immediate job searching.""",
        )