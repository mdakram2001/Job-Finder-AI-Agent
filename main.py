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

async def main():
    final_state = await app.ainvoke(initial_state)

    # 3. Print the final results nicely
    print("\n--- ELIGIBILITY RESULTS ---\n")
    for result in final_state.get("eligibility_results", []):
        # print(f"Job: {result.job.job_title} at {result.job.company}")
        print(f"Eligible: {result.is_eligible}")
        print(f"Match Percentage: {result.percentage_match}%")
        if not result.is_eligible:
            print(f"Reason: {result.reason}")
        print("-" * 30)

if __name__ == "__main__":
    asyncio.run(main())
