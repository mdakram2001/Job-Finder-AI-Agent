from pypdf import PdfReader
from states.graph_state import State
from schemas.resume_schema import ResumeSchema
from langchain_core.messages import HumanMessage, SystemMessage
# from llms.huggingface import model
from llms.ollama import model



# ---------------------
# i) Node 1:
# ---------------------
PROMPT_1 = """
You are an expert resume parser and information extraction assistant.

Your task is to analyze the applicant's resume and extract only the information that is explicitly stated or can be reasonably inferred from the resume and any additional information provided by the user.

Populate the `ResumeSchema` exactly according to its field definitions.

Rules:
- Follow the schema field names exactly. Do not invent or rename fields.
- For nested objects (such as projects), use the exact field names defined in the schema (e.g., `project_title`, `project_description`, `project_skills`).
- If a project title is not explicitly mentioned, generate a short, descriptive title based on the project's description.
- Extract all relevant skills, job roles, experience, locations, projects, education status, and other applicable information.
- If the user provides additional information outside the resume, merge it with the extracted resume information. User-provided information takes precedence if there is a conflict.
- If a field cannot be determined, leave it as `null` rather than guessing.
- Do not fabricate information that cannot be reasonably inferred from the provided content.
- Return a response that strictly conforms to the provided `ResumeSchema`.
"""
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
        SystemMessage(content=PROMPT_1),
        HumanMessage(content=f"Analyze the following document:\n\n{text}")
        ])
    return {"resume": parsed_resume}
    



