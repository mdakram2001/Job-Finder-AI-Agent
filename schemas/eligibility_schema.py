from pydantic import BaseModel, Field
from typing import List, Optional
from schemas.job_schema import JobSchema
from schemas.resume_schema import ResumeSchema

class EligibilitySchema(BaseModel):
    # job: JobSchema = Field(..., description="Job/Internship details")
    # resume: ResumeSchema = Field(..., description="Applicant's resume details")
    # skill_match: SkillMatchSchema = Field(..., description="Skill match details between the applicant and the job/internship")
    percentage_match: Optional[float] = Field(default=None, ge=0, le=100, description="Overall percentage match between the applicant and the job/internship")
    is_eligible: bool = Field(..., description="Whether the applicant is eligible for the job/internship based on skills, experience, and preferences")
    reason: Optional[str] = Field(default=None, description="Reason for ineligibility if the applicant is not eligible for the job/internship")
