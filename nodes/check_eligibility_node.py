from typing import TypedDict, List
from states.graph_state import State
from langchain_core.messages import SystemMessage, HumanMessage
from schemas.eligibility_schema import EligibilitySchema
from prompts.prompt import JOB_ELIGIBILITY_EVALUATION_PROMPT
# from llms.huggingface import model
from llms.ollama import model


def check_eligibility(state: State):

    structured_llm = model.with_structured_output(EligibilitySchema, method="function_calling")
    final_results = []

    for i in state['jobs']:
        eligibility_result = structured_llm.invoke([
            SystemMessage(content=JOB_ELIGIBILITY_EVALUATION_PROMPT),
            HumanMessage(content=f"Here is the resume :\n\n{state['resume']} \n\n Here is the job :\n\n{i}")
        ])
        final_results.append(eligibility_result)

    return {"eligibility_results": final_results}
