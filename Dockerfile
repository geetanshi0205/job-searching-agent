FROM python:3.12-slim

WORKDIR /app

# Install Node.js and npm for the Airbnb MCP server
RUN apt-get update && apt-get install -y \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt to the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Create logs directory
RUN mkdir -p logs

# Expose the port used by the agent
EXPOSE 8001

# Command to run the application
CMD ["python3", "job_search_adapter.py"]