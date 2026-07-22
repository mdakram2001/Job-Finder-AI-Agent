from typing import Annotated, Literal, TypedDict
from operator import add
from schemas.resume_schema import ResumeSchema
from schemas.job_schema import JobSchema
from schemas.eligibility_schema import EligibilitySchema
from pydantic import Field


class State(TypedDict):
    resume_path: str
    job_roles: Annotated[
    list[str],
    Field(
        default=None,
        description="List of job roles the applicant is qualified for or interested in, inferred from the resume.",
        examples=[["Data Scientist", "Machine Learning Engineer"]],
        ),
    ]
    resume: ResumeSchema | None
    jobs: Annotated[list[JobSchema], add]
    eligibility_results: Annotated[list[EligibilitySchema], add]