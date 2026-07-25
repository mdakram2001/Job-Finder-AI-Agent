from typing import TypedDict, List
from states.graph_state import State
from langchain_core.messages import SystemMessage, HumanMessage
from schemas.eligibility_schema import EligibilitySchema
# from llms.huggingface import model
from llms.ollama import model



PROMPT_4 = """
    You are an expert recruitment eligibility evaluator.

    Your task is to assess whether a candidate is eligible for a job by comparing the candidate's resume with the provided job description and any additional hiring criteria.

    Instructions:
    1. Analyze the candidate's qualifications, skills, experience, education and other relevant information against the job requirements.
    2. Calculate an overall match percentage (0–100) representing how well the candidate meets the requirements.
    3. The eligibility threshold is 85%.
    - If the match percentage is **85% or higher**, mark the candidate as **eligible**.
    - If the match percentage is **below 85%**, mark the candidate as **not eligible**.
    4. If the candidate is not eligible, provide a concise explanation highlighting the primary reasons for rejection (e.g., missing required skills, insufficient experience, missing certifications, education mismatch, etc.).
    5. Base your evaluation only on the information provided. Do not assume qualifications that are not explicitly mentioned.
    6. Return the result strictly in the format defined by the `EligibilitySchema`.

    Evaluation Guidelines:
    - Prioritize required qualifications over preferred qualifications.
    - Consider transferable skills when appropriate, but do not overestimate their relevance.
    - Penalize missing mandatory requirements appropriately.
    - Keep the rejection reason brief (1–3 sentences) and specific.

    Your output must conform exactly to the `EligibilitySchema`.
"""
def check_eligibility(state: State):

    structured_llm = model.with_structured_output(EligibilitySchema, method="function_calling")
    final_results = []

    for i in state['jobs']:
        eligibility_result = structured_llm.invoke([
            SystemMessage(content=PROMPT_4),
            HumanMessage(content=f"Here is the resume :\n\n{state['resume']} \n\n Here is the job :\n\n{i}")
        ])
        final_results.append(eligibility_result)

    return {"eligibility_results": final_results}
