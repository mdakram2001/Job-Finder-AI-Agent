from schemas.job_schema import JobSchema
from states.graph_state import State
# from llms.huggingface import model
from llms.ollama import model
from langchain_core.messages import SystemMessage, HumanMessage
from prompts.prompt import JOB_SCHEMA_FILLING_PROMPT
import asyncio
import sys
import os

# -----------------------------
# Path Setting for Additional Imports
# -----------------------------
# Add the scraper folder to Python's search path
sys.path.append(os.path.abspath("tools/linkedin_scraper"))

# Additional Imports
from linkedin_scraper import scrape_jobs
from linkedin_scraper.config.settings import settings


# -----------------------------
# iii) Node 3:
# -----------------------------

async def linkedin_job_search_node(state: State) -> dict:
    
    job_roles = state.get('job_roles', [])
    all_jobs = []

    settings.search.filters.time_posted = "r86400"

    structured_llm = model.with_structured_output(JobSchema, method="function_calling")
    

    for i in job_roles:

        jobs = await scrape_jobs(
        keywords = i, 
        location= "Remote", 
        max_results=10,
        headless=True, # Set to False if you want to watch the browser
        )
    
        all_jobs.extend(jobs)

        

    return {
        "jobs": [(
            structured_llm.invoke([
                SystemMessage(content=JOB_SCHEMA_FILLING_PROMPT),
                HumanMessage(content=f"Here is the data :\n\n{job}")
            ])
            ) for job in all_jobs]
    }