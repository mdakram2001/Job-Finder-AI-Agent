import os
from dotenv import load_dotenv
from graph.graph import app

# Load environment variables from .env file
load_dotenv()

# 1. Define the initial state with the path to a resume PDF on your computer
initial_state = {
    "resume_path": "resume.pdf" # <-- REPLACE THIS with the path to your actual PDF
}

# 2. Run the compiled graph. 
# We use await app.ainvoke() because your scraper node is async
import asyncio
import json
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
        with open("jobs.json", "a", encoding="utf-8") as f:
            f.write(json.dumps(record, indent=2))
            f.write("\n")
            print("================== Job Saved =====================")
        

if __name__ == "__main__":
    asyncio.run(main())
