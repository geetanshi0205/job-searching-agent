# Job Search Agent - uAgent Adapter

This project wraps a Job Search Agent in a uAgent adapter, making it accessible as a networked AI agent that can find and match job opportunities to user skills and preferences.

## Features

- **Multi-Agent Workflow**: Uses specialized agents for job market research, skills analysis, and opportunity curation
- **Job Market Research**: Analyzes current job markets, salary ranges, and industry trends
- **Skills Matching**: Matches user skills and experience with available job opportunities
- **Opportunity Curation**: Curates and presents the best job opportunities with direct application links
- **Direct Application Links**: Provides clickable URLs for immediate job applications
- **Networked Access**: Exposed as a uAgent for integration with other agents and systems

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment Variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

3. **Required API Keys**:
   - OpenAI API key for CrewAI agents
   - Serper API key for web search functionality
   - Agentverse API key for uAgent registration

## Usage

### Running the Agent

```bash
python job_search_adapter.py
```

The agent will register itself on port 8001 and be available for queries through the Agentverse network.

### Query Parameters

- `job_title` (required): Job title or position you're looking for
- `location` (required): Preferred job location
- `experience_level` (required): Your experience level
- `skills` (required): Your skills and technical abilities
- `career_goals` (optional): Your career objectives and goals
- `preferred_industry` (optional): Industry preferences
- `salary_range` (optional): Desired salary range
- `user_preferences` (optional): Additional preferences (remote work, company size, etc.)

### Example Query

```python
query = {
    "job_title": "Senior Software Engineer",
    "location": "San Francisco",
    "experience_level": "5+ years",
    "skills": "Python, React, AWS, Docker, Kubernetes",
    "career_goals": "Lead technical teams and work on AI/ML projects",
    "preferred_industry": "Technology",
    "salary_range": "$120,000 - $180,000",
    "user_preferences": "Remote work, startup environment, equity compensation"
}
```

## Architecture

The adapter consists of three main components:

1. **JobSearchCrew**: Job Search Agent implementation with specialized agents
   - Job Market Researcher: Market analysis and opportunity discovery
   - Skills Analyzer: Skills matching and career guidance
   - Opportunity Curator: Job curation and application strategy

2. **uAgent Wrapper**: Network interface using CrewaiRegisterTool
   - Handles parameter validation
   - Manages agent communication
   - Provides Agentverse registration

3. **Task Pipeline**: Sequential workflow for job searching
   - Job market research → Skills analysis → Opportunity curation

## Agents

### Job Market Researcher
- **Role**: Job Market Research Specialist
- **Goal**: Search and analyze job markets for the best opportunities
- **Tools**: Web search via Serper API for current job listings

### Skills Analyzer
- **Role**: Skills Analysis and Matching Expert  
- **Goal**: Analyze user skills and match them with job requirements
- **Expertise**: Career counseling and skills assessment

### Opportunity Curator
- **Role**: Job Opportunity Curator
- **Goal**: Curate and present the best job opportunities with strategies
- **Expertise**: Career advising and job search strategy

## Output

The agent returns a comprehensive job search report including:
- Current job market analysis and trends
- Skills assessment and gap analysis
- Top 10 curated job opportunities with direct application links
- Company profiles and culture insights
- Clickable URLs for immediate job applications
- Application strategies and interview tips
- Salary expectations and market positioning
- Career development recommendations

## Author

**Geetanshi Goel**
- GitHub: [@geetanshi](https://github.com/geetanshi0205)
- LinkedIn: [Geetanshi Goel](https://www.linkedin.com/in/geetanshi-goel-49ba5832b/)