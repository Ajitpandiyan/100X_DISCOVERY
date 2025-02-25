import pytest
from httpx import AsyncClient
from app.main import app
from app.models.profile import ProfileCreate


@pytest.mark.asyncio
async def test_create_profile():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        profile_data = {
            "name": "Test User",
            "bio": "Test Bio",
            "skills": ["Python", "Testing"],
            "interests": ["AI", "Development"],
            "github_url": "https://github.com/testuser",
            "linkedin_url": "https://linkedin.com/in/testuser",
        }

        response = await ac.post("/api/v1/profiles/", json=profile_data)
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == profile_data["name"]
        assert "id" in data


@pytest.mark.asyncio
async def test_get_profile():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # First create a profile
        profile_data = {
            "name": "Test User",
            "bio": "Test Bio",
            "skills": ["Python", "Testing"],
            "interests": ["AI", "Development"],
        }

        create_response = await ac.post("/api/v1/profiles/", json=profile_data)
        created_profile = create_response.json()

        # Then get the profile
        response = await ac.get(f"/api/v1/profiles/{created_profile['id']}")
        assert response.status_code == 200
        assert response.json()["id"] == created_profile["id"]
