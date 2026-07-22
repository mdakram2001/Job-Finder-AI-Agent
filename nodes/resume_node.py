from pypdf import PdfReader
from states.graph_state import State
from schemas.resume_schema import ResumeSchema
from langchain_core.messages import HumanMessage, SystemMessage



# -----------------------------
# i) Node 1:
# -----------------------------
PROMPT_1 = """
You are text extractor or text analyser. Your task is to analyze the applicant's resume and fill the content of the ResumeSchema based on the information provided in the resume. If user provides some information, use it to populate the schema and add the resume information to it.
"""
def resume_node(state: State) -> dict:

    # ----------------------------- Getting the text of PDF ------------------------------

    reader = PdfReader(state["resume_path"])
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"


    # ----------------------------- Filling the ResumeSchema ------------------------------

    structured_llm = model.with_structured_output(ResumeSchema, method='json_schema')
    parsed_resume = structured_llm.invoke([
        SystemMessage(content=PROMPT_1),
        HumanMessage(content=f"Analyze the following document:\n\n{text}")
        ])
    return {"resume": parsed_resume}

