"""Test module for semantic search functionality."""

import pytest
from httpx import AsyncClient
import json
from unittest.mock import patch, AsyncMock, MagicMock

from app.main import app
from app.services.groq_service import GroqService
from app.models.profile import Profile


class MockProfile:
    """Mock Profile class for testing."""

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def dict(self):
        """Return a dictionary representation of the profile."""
        return {k: v for k, v in self.__dict__.items()}


@pytest.mark.asyncio
async def test_search_endpoint_returns_matches():
    """Test that the search endpoint returns matches."""
    # Create test profiles
    test_profiles = [
        {
            "id": "1",
            "name": "AI Developer",
            "bio": "Expert in machine learning",
            "skills": ["Python", "ML", "AI"],
            "interests": ["Deep Learning", "NLP"],
        },
        {
            "id": "2",
            "name": "Frontend Developer",
            "bio": "Building beautiful UIs",
            "skills": ["JavaScript", "React", "CSS"],
            "interests": ["UI/UX", "Web Design"],
        },
    ]

    # Mock the profile service to return test profiles
    with patch(
        "app.services.profile_service.ProfileService.list_profiles",
        new_callable=AsyncMock,
    ) as mock_list_profiles:
        # Set up the mock to return our test profiles
        mock_list_profiles.return_value = [
            MockProfile(**profile) for profile in test_profiles
        ]

        # Mock the Groq service to return expected results
        with patch(
            "app.services.groq_service.GroqService.get_semantic_search_results",
            new_callable=AsyncMock,
        ) as mock_search:
            # Set up the mock to return expected search results
            mock_search.return_value = [
                {
                    "id": "1",
                    "name": "AI Developer",
                    "bio": "Expert in machine learning",
                    "skills": ["Python", "ML", "AI"],
                    "interests": ["Deep Learning", "NLP"],
                    "score": 95,
                    "match_reason": "Strong match on AI skills and interests",
                }
            ]

            # Test the search endpoint
            async with AsyncClient(app=app, base_url="http://test") as ac:
                response = await ac.get("/api/v1/search/?query=machine learning expert")

                # Verify the response
                assert response.status_code == 200
                data = response.json()
                assert "matches" in data
                assert len(data["matches"]) == 1
                assert data["matches"][0]["id"] == "1"
                assert "score" in data["matches"][0]
                assert "match_reason" in data["matches"][0]


@pytest.mark.asyncio
async def test_groq_service_fallback():
    """Test that the Groq service falls back to basic search if API fails."""
    # Create a Groq service instance
    service = GroqService()

    # Create test profiles
    test_profiles = [
        {
            "id": "1",
            "name": "AI Developer",
            "bio": "Expert in machine learning",
            "skills": ["Python", "ML", "AI"],
            "interests": ["Deep Learning", "NLP"],
        },
        {
            "id": "2",
            "name": "Frontend Developer",
            "bio": "Building beautiful UIs",
            "skills": ["JavaScript", "React", "CSS"],
            "interests": ["UI/UX", "Web Design"],
        },
    ]

    # Mock the httpx client to raise an exception
    with patch("httpx.AsyncClient.post", side_effect=Exception("API Error")):
        # Call the method with a query that should match the first profile
        results = await service.get_semantic_search_results(
            "machine learning", test_profiles
        )

        # Verify that fallback search worked
        assert len(results) > 0
        assert results[0]["id"] == "1"  # The AI Developer should match
        assert "score" in results[0]
        assert results[0]["match_reason"] == "Text match"


@pytest.mark.asyncio
async def test_health_endpoint():
    """Test that the health endpoint returns healthy status."""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/v1/search/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}
