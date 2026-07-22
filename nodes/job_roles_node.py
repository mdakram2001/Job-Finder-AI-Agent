from states.graph_state import State

# -----------------------------
# ii) Node 2:
# -----------------------------
PROMPT_2 = """
You are a job and internship resume analyzer. Your task is to analyze the applicant's details provided through a Resume Schema/Dictionary and predict the applicant's most suitable job roles, internship roles. Base your analysis solely on the information present in the resume. Do not make assumptions or infer qualifications that are not supported by the resume.

For each predicted role:
- Ensure it is relevant to the applicant's education, skills, projects etc. Don't be too much strict
- Include only roles for which the applicant appears reasonably qualified (almost 85-95 %).
- Prefer specific role titles (e.g., "Machine Learning Engineer", "Backend Developer", "Data Analyst") over generic titles (e.g., "Engineer", "Developer").
- Exclude unrelated or unrealistic roles.

Return the results as a list of strings. example : ["Data Scientist", "Machine Learning Engineer"]
"""
def find_job_roles(state: State) -> dict:

    # ----------------------------- Getting the Resume Details from the State ------------------------------

    resume = state['resume']

    # ---------------------------------- Getting job roles from the model ----------------------------------

    parsed_roles = model.invoke([
        
        SystemMessage(content=PROMPT_2),
        HumanMessage(content=f"Here is the Details :\n\n{resume}")
        
    ])
    all_roles = state['job_roles'].append(parsed_roles)

    return {"jobs_roles" : all_roles}

