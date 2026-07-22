from linkedin_jobs import scrape_jobs, settings
from schemas.job_schema import JobSchema
from states.graph_state import State
import asyncio


# -----------------------------
# iii) Node 3:
# -----------------------------
PROMPT_3 = """
    You are given either a Python dictionary or JSON object containing job-related information. Your task is to analyze the provided data and populate the JobSchema accordingly.

    1. Map the available fields from the input data to the corresponding fields in JobSchema.
    2. If a field is already correctly populated, leave it unchanged.
    3. If a field is missing, empty, or incorrectly populated, infer and fill it using the information available in the input data.
    4. Use contextual understanding to extract or generate values for fields such as job_description, job_title, skills, location, and any other relevant schema fields whenever possible.
    5. Do not overwrite valid existing values with inferred ones.
    6. Return the completed JobSchema with all fields populated as accurately as possible based on the provided data. 
"""
async def linkedin_job_search_node(state: State) -> dict:
    
    job_roles = state['jobs_roles']
    all_jobs = []

    settings.search.filters.time_posted = "r86400"

    structured_llm = model.with_structured_output(JobSchema, method='json_schema')
    
    for i in jobs:

        jobs = await scrape_jobs(
        keywords = i, 
        location= state[''], 
        max_results=10,
        headless=True, # Set to False if you want to watch the browser
        )
    
        all_jobs = all_jobs + jobs

        

    return {
        "jobs": [JobSchema.model_validate(
            structured_llm.invoke([
                SystemMessage(content=PROMPT_3),
                HumanMessage(content=f"Here is the data :\n\n{job}")
            ])
            ) for job in all_jobs]
    }