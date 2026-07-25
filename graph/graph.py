from langgraph.graph import StateGraph, START, END
from states.graph_state import State
from nodes.resume_node import resume_node
from nodes.job_roles_node import find_job_roles
from nodes.linkedin_search_node import linkedin_job_search_node
from nodes.check_eligibility_node import check_eligibility


graph = StateGraph(State)

graph.add_node("resume_node", resume_node)
graph.add_node("find_job_roles", find_job_roles)
graph.add_node("linkedin_job_search_node", linkedin_job_search_node)
graph.add_node("check_eligibility", check_eligibility)


graph.add_edge(START, "resume_node")
graph.add_edge("resume_node", "find_job_roles")
graph.add_edge("find_job_roles", "linkedin_job_search_node")
graph.add_edge("linkedin_job_search_node", "check_eligibility")
graph.add_edge("check_eligibility", END)

app = graph.compile()