from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class ProfileBase(BaseModel):
    name: str
    bio: str
    skills: List[str]
    interests: List[str]
    github_url: Optional[str] = None
    linkedin_url: Optional[str] = None

class ProfileCreate(ProfileBase):
    pass

class Profile(ProfileBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "id": "user123",
                "name": "John Doe",
                "bio": "Full-stack developer passionate about AI",
                "skills": ["Python", "React", "FastAPI"],
                "interests": ["Machine Learning", "Web Development"],
                "github_url": "https://github.com/johndoe",
                "linkedin_url": "https://linkedin.com/in/johndoe"
            }
        }