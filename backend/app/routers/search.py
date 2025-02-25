"""Search router module.

This module provides endpoints for searching profiles using semantic search via Groq API.
"""

from typing import Dict, List, Any

from fastapi import APIRouter, HTTPException, Query

from app.services.profile_service import ProfileService
from app.services.groq_service import GroqService

router = APIRouter()
profile_service = ProfileService()
groq_service = GroqService()


@router.get("/")
async def search_profiles(
    query: str = Query(..., description="Search query for matching profiles")
) -> Dict[str, List[Dict[str, Any]]]:
    """Search for profiles based on a text query using semantic search.

    The search uses Groq's LLM to understand the semantic meaning of:
    - Name
    - Bio
    - Skills (weighted higher)
    - Interests (weighted medium)

    Args:
        query: Search string to match against profiles

    Returns:
        Dict[str, List[Dict]]: List of matching profiles with scores and match reasons

    Raises:
        HTTPException: If search fails
    """
    try:
        # Get all profiles
        profiles = await profile_service.list_profiles()
        
        # Convert profiles to dictionaries
        profile_dicts = [profile.dict() for profile in profiles]
        
        # Use Groq for semantic search
        matches = await groq_service.get_semantic_search_results(query, profile_dicts)

        return {"matches": matches}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to search profiles: {str(e)}",
        )


@router.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check endpoint.

    Returns:
        Dict[str, str]: Health status response
    """
    return {"status": "healthy"}