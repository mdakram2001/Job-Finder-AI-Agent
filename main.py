import os
import json
import asyncio
from dotenv import load_dotenv
from graph.graph import app
from schemas.job_schema import JobSchema
from schemas.eligibility_schema import EligibilitySchema
from utilities.save_jobs import save_jobs

# Load environment variables from .env file
load_dotenv()

# 1. Define the initial state with the path to a resume PDF on your computer
initial_state = {
    "resume_path": "resume.pdf" # <-- REPLACE THIS with the path to your actual PDF
}

# 2. Run the compiled graph. 
# We use await app.ainvoke() because your scraper node is async

async def main():

    final_state = await app.ainvoke(initial_state)

    # 3. Print the final results nicely
    print("\n--- ELIGIBILITY RESULTS ---\n")
    for result in final_state.get("eligibility_results", []):

        job: JobSchema = result[0]
        eligibility: EligibilitySchema = result[1]

        record = {
            "job": job.model_dump(),
            "eligibility": eligibility.model_dump(),
        }

        save_jobs(record)

if __name__ == "__main__":
    asyncio.run(main())
