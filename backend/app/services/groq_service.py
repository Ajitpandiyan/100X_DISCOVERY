from typing import List, Dict
import httpx
from app.core.config import settings

class GroqService:
    def __init__(self):
        self.api_key = settings.GROQ_API_KEY
        self.base_url = "https://api.groq.com/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    async def search_profiles(self, query: str, profiles: List[Dict]) -> List[Dict]:
        system_prompt = """You are a profile matching assistant. Given a search query and a list of profiles, 
        return the most relevant profiles based on skills, interests, and bio. Explain why each profile matches."""
        
        user_prompt = f"""Search Query: {query}
        Profiles: {profiles}
        
        Return only the most relevant profiles with explanation."""

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json={
                    "model": "mixtral-8x7b-32768",
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    "temperature": 0.7,
                    "max_tokens": 1000
                }
            )
            response.raise_for_status()
            return response.json()