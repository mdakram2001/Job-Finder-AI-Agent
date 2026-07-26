from states.graph_state import State
# from llms.huggingface import model
from llms.ollama import model
from langchain_core.messages import SystemMessage, HumanMessage
from prompts.prompt import JOB_ROLE_EXTRACT_PROMPT
import json
import re


# -----------------------------
# ii) Node 2:
# -----------------------------

def find_job_roles(state: State) -> dict:

    # ----------------------------- Getting the Resume Details from the State ------------------------------

    resume = state['resume']
    state['job_roles'] = []

    # ---------------------------------- Getting job roles from the model ----------------------------------

    parsed_roles = model.invoke([
        
        SystemMessage(content=JOB_ROLE_EXTRACT_PROMPT),
        HumanMessage(content=f"Here is the Details :\n\n{resume}")
        
    ])

    content = parsed_roles.content
    try:
        # Extract the JSON list from the string response
        match = re.search(r'\[.*\]', content, re.DOTALL)
        if match:
            roles_list = json.loads(match.group(0))
        else:
            roles_list = [content.strip()]
    except Exception:
        roles_list = [content.strip()]

    return {"job_roles" : roles_list}



