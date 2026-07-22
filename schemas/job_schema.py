from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class JobSchema(BaseModel):
    job_id: str = Field(default=None, description="Id of the job provided in the job data. If not present then None.")
    job_title: str = Field(..., min_length=1, max_length=100, description="Job/Internship title")
    company: Optional[CompanySchema] = Field(default=None, description="Company offering the job/internship")
    job_location: Optional[str] = Field(default=None, description="Location of the job/internship")
    job_url: Optional[str] = Field(default=None, description="Link to the job/internship posting")
    job_posted_date: Optional[date] = Field(default=None, description="Date when the job/internship was posted")
    job_description: str = Field(..., description="Job/Internship description")
    seniority_level: str = Field(default=None, description="Required seniority level of the job", examples=["Entry level", "Freshers"])
    job_type: Optional[Literal["Full-time", "Part-time", "Contract", "Temporary"]] = Field(default=None, description="Type of the job/internship")
    total_applicants: Optional[int] = Field(default=None, ge=0, description="Total number of applicants for the job/internship")
    workplace_type: str = Field(default=None, description="Type of the workplace", examples=["On site", "Hybrid", "Remote"])
    required_skills: List[str] = Field(..., description="List of required skills for the job/internship", examples=["Python", "Machine Learning"])
    required_experience: Optional[str] = Field(default=None, description="Required experience for the job/internship")
    is_internship: Optional[bool] = Field(default=None, description="Whether the job is an internship")
    is_remote: Optional[bool] = Field(default=None, description="Whether the job is remote")
