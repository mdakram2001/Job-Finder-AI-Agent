from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from schemas.project_schema import ProjectSchema

class ResumeSchema(BaseModel):
    job_roles: Optional[List[str]] = Field(default=None, description="List of job roles the applicant is interested in or can apply according to the resume", examples=["Data Scientist", "Machine Learning Engineer"])
    applicant_skills: Optional[List[str]] = Field(default=None, description="List of applicant's skills", examples=["Python", "N8N", "Machine Learning"])
    applicant_experience: Optional[str] = Field(default=None, description="Applicant's experience")
    location_choices: Optional[List[str]] = Field(default=None, description="List of applicant's preferred locations")
    projects: Optional[List[ProjectSchema]] = Field(default=None, description="List of projects/internships")
    only_remote: Optional[bool] = Field(default=None, description="Whether the applicant is only looking for remote jobs")
    only_internship: Optional[bool] = Field(default=None, description="Whether the applicant is only looking for internships")
    is_student: Optional[bool] = Field(default=None, description="Whether the applicant is a student")
    extra_information: Optional[Dict[str, Any]] = Field(default=None, description="Any extra information about the applicant")
