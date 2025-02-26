"""Search router module.

This module provides endpoints for searching profiles using semantic search via Groq API.
"""

import logging
from typing import Any, Dict, List

from app.services.groq_service import GroqService
from app.services.profile_service import ProfileService
from fastapi import APIRouter, Body, HTTPException, Query

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()
profile_service = ProfileService()
groq_service = GroqService()


@router.get("/")
async def search_profiles_get(
    query: str = Query(..., description="Search query for matching profiles")
) -> Dict[str, List[Dict[str, Any]]]:
    """Search for profiles based on a text query using semantic search (GET method).

    See POST method for more details.
    """
    return await _perform_search(query)


@router.post("/")
async def search_profiles_post(
    query_data: Dict[str, str] = Body(
        ..., example={"query": "experienced AI researcher"}
    )
) -> Dict[str, List[Dict[str, Any]]]:
    """Search for profiles based on a text query using semantic search.

    The search uses Groq's LLM to understand the semantic meaning of:
    - Name
    - Bio
    - Skills (weighted higher)
    - Interests (weighted medium)

    Args:
        query_data: JSON object with a 'query' field containing the search string

    Returns:
        Dict[str, List[Dict]]: List of matching profiles with scores and match reasons

    Raises:
        HTTPException: If search fails or query is missing
    """
    if "query" not in query_data:
        raise HTTPException(
            status_code=400,
            detail="Missing required field 'query' in request body",
        )

    return await _perform_search(query_data["query"])


async def _perform_search(query: str) -> Dict[str, List[Dict[str, Any]]]:
    """Internal function to perform the search logic.

    Args:
        query: Search string to match against profiles

    Returns:
        Dict with matches

    Raises:
        HTTPException on error
    """
    logger.info(f"Performing semantic search for query: '{query}'")

    try:
        # Get all profiles
        profiles = await profile_service.list_profiles()

        if not profiles:
            logger.warning("No profiles found in database")
            return {"matches": []}

        # Convert profiles to dictionaries
        profile_dicts = [profile.dict() for profile in profiles]
        logger.info(f"Found {len(profile_dicts)} profiles to search through")

        # Use Groq for semantic search
        matches = await groq_service.get_semantic_search_results(query, profile_dicts)
        logger.info(f"Search complete. Found {len(matches)} matching profiles")

        return {"matches": matches}
    except Exception as e:
        logger.error(f"Search failed: {str(e)}", exc_info=True)
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
