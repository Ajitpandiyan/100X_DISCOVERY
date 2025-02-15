from datetime import datetime, timedelta
from typing import Optional
import jwt
from app.core.config import settings

class SecurityService:
    @staticmethod
    def create_api_key() -> str:
        """Generate a secure API key for profile owners"""
        return jwt.encode(
            {
                "created_at": datetime.utcnow().isoformat(),
                "exp": datetime.utcnow() + timedelta(days=365)
            },
            settings.SECRET_KEY,
            algorithm="HS256"
        )

    @staticmethod
    def verify_api_key(api_key: str) -> bool:
        try:
            jwt.decode(api_key, settings.SECRET_KEY, algorithms=["HS256"])
            return True
        except:
            return False