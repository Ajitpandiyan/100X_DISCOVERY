"""Test configuration for pytest."""

import os
from unittest.mock import patch

import pytest


@pytest.fixture(autouse=True)
def mock_env_variables():
    """Mock environment variables for testing."""
    with patch.dict(
        os.environ,
        {
            "GROQ_API_KEY": "test_groq_api_key",
            "ENVIRONMENT": "test",
            "BACKEND_CORS_ORIGINS": '["http://localhost:8501"]',
        },
    ):
        yield
