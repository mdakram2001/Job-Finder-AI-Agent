from typing import Annotated, TypedDict
from operator import add
from schemas.resume_schema import ResumeSchema
from schemas.job_schema import JobSchema
from schemas.eligibility_schema import EligibilitySchema


class State(TypedDict):
    resume_path: str
    job_roles: Annotated[list[str], add]
    resume: ResumeSchema | None
    jobs: Annotated[list[JobSchema], add]
    eligibility_results: Annotated[list[EligibilitySchema], add]