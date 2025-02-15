from fastapi import APIRouter, HTTPException, status
from typing import List
import uuid
from app.models.profile import Profile, ProfileCreate
from app.services.profile_service import ProfileService

router = APIRouter()
profile_service = ProfileService()

@router.post("/", response_model=Profile, status_code=status.HTTP_201_CREATED)
async def create_profile(profile: ProfileCreate):
    profile_dict = profile.dict()
    profile_dict["id"] = str(uuid.uuid4())
    return await profile_service.create_profile(profile_dict)

@router.get("/{profile_id}", response_model=Profile)
async def get_profile(profile_id: str):
    profile = await profile_service.get_profile(profile_id)
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )
    return profile

@router.get("/", response_model=List[Profile])
async def list_profiles():
    return await profile_service.list_profiles()