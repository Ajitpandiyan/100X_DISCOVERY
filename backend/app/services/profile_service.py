import json
import aiofiles
from typing import List, Dict, Optional
from app.models.profile import Profile
from pathlib import Path
import os


class ProfileService:
    def __init__(self):
        # Get the absolute path to the backend directory
        backend_dir = Path(__file__).parent.parent.parent
        self.data_file = backend_dir / "data" / "profiles.json"
        self.data_file.parent.mkdir(exist_ok=True)
        if not self.data_file.exists():
            self.data_file.write_text("[]")

    async def _read_profiles(self) -> List[Dict]:
        async with aiofiles.open(self.data_file, mode='r') as f:
            content = await f.read()
            return json.loads(content)

    async def _write_profiles(self, profiles: List[Dict]) -> None:
        async with aiofiles.open(self.data_file, mode='w') as f:
            await f.write(json.dumps(profiles, indent=2))

    async def create_profile(self, profile_data: Dict) -> Profile:
        try:
            profiles = await self._read_profiles()
            profiles.append(profile_data)
            await self._write_profiles(profiles)
            return Profile(**profile_data)
        except Exception as e:
            print(f"Error creating profile: {str(e)}")
            raise

    async def get_profile(self, profile_id: str) -> Optional[Profile]:
        profiles = await self._read_profiles()
        for profile in profiles:
            if profile["id"] == profile_id:
                return Profile(**profile)
        return None

    async def list_profiles(self) -> List[Profile]:
        profiles = await self._read_profiles()
        return [Profile(**profile) for profile in profiles]
