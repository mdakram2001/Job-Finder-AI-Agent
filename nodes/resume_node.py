from pypdf import PdfReader
from states.graph_state import State
from schemas.resume_schema import ResumeSchema
from langchain_core.messages import HumanMessage, SystemMessage
# from llms.huggingface import model
from llms.ollama import model
from prompts.prompt import RESUME_TEXT_EXTRACT_PROMPT



# ---------------------
# i) Node 1:
# ---------------------
def resume_node(state: State) -> dict:

    # --------------------- Getting the text of PDF ---------------------

    reader = PdfReader(state["resume_path"])
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"


    # --------------------- Filling the ResumeSchema ---------------------

    structured_llm = model.with_structured_output(ResumeSchema, method="function_calling")
    parsed_resume = structured_llm.invoke([
        SystemMessage(content=RESUME_TEXT_EXTRACT_PROMPT),
        HumanMessage(content=f"Analyze the following document:\n\n{text}")
        ])
    return {"resume": parsed_resume}
    



