"""Profile data models.

This module contains the Pydantic models for user profiles in the 100X Discovery Platform.
"""

from typing import List, Optional

from pydantic import BaseModel, Field
from datetime import datetime


class ProfileBase(BaseModel):
    """Base profile model with common attributes."""

    name: str = Field(..., description="Full name of the user")
    bio: str = Field(..., description="Brief biography or description")
    skills: List[str] = Field(default_factory=list, description="List of technical skills")
    interests: List[str] = Field(
        default_factory=list, description="List of professional interests"
    )
    github_url: Optional[str] = None
    linkedin_url: Optional[str] = None


class ProfileCreate(ProfileBase):
    """Profile creation model."""

    pass


class ProfileUpdate(ProfileBase):
    """Profile update model with optional fields."""

    name: Optional[str] = Field(None, description="Full name of the user")
    bio: Optional[str] = Field(None, description="Brief biography or description")
    skills: Optional[List[str]] = Field(None, description="List of technical skills")
    interests: Optional[List[str]] = Field(
        None, description="List of professional interests"
    )


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