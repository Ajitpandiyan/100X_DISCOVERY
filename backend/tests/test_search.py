import pytest
from httpx import AsyncClient
from app.main import app
from fastapi.testclient import TestClient


@pytest.mark.asyncio
async def test_search_profiles():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Create a test profile first
        profile_data = {
            "name": "AI Developer",
            "bio": "Expert in machine learning",
            "skills": ["Python", "ML", "AI"],
            "interests": ["Deep Learning", "NLP"],
        }
        await ac.post("/api/v1/profiles/", json=profile_data)

        # Test search
        response = await ac.get("/api/v1/search/?query=machine learning expert")
        assert response.status_code == 200
        data = response.json()
        assert "choices" in data


client = TestClient(app)


def test_search_endpoint_exists():
    """Test that the search endpoint exists"""
    response = client.get("/api/v1/search/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
