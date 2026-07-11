from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class ProjectSchema(BaseModel):
    project_title: str = Field(..., min_length=1, max_length=100, description="Title of the project/internship", examples=["AI Chatbot Development"])
    project_description: str = Field(..., description="Description of the project/internship")
    project_skills: List[str] = Field(..., description="List of skills/technologies used in the project/internship", examples=["Python", "Machine Learning"])
    duration_months: Optional[int] = Field(default=None, description="Duration of the project/internship in months (e.g., 3 for 3 months)")
    project_level: Optional[Literal["Beginner", "Intermediate", "Advanced"]] = Field(default=None, description="Level of the project/internship")
