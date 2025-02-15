from fastapi import APIRouter, Query
from typing import List, Dict
from app.services.profile_service import ProfileService

router = APIRouter()
profile_service = ProfileService()

@router.get("/")
async def search_profiles(
    query: str = Query(..., description="Search query for matching profiles")
) -> Dict:
    # Get all profiles
    profiles = await profile_service.list_profiles()
    
    # Convert query to lowercase for case-insensitive matching
    query = query.lower()
    
    # Simple text matching
    matches = []
    for profile in profiles:
        profile_dict = profile.dict()
        score = 0
        
        # Check name
        if query in profile_dict["name"].lower():
            score += 1
            
        # Check bio
        if query in profile_dict["bio"].lower():
            score += 1
            
        # Check skills
        for skill in profile_dict["skills"]:
            if query in skill.lower():
                score += 2
                
        # Check interests
        for interest in profile_dict["interests"]:
            if query in interest.lower():
                score += 1.5
                
        if score > 0:
            profile_dict["score"] = score
            matches.append(profile_dict)
    
    # Sort by score
    matches.sort(key=lambda x: x["score"], reverse=True)
    
    return {"matches": matches}