"""Test suite for 100X Discovery Platform Backend.

This package contains test modules for:
- Profile management
- Search functionality
- API endpoints
- Data integrity
"""

import os
from pathlib import Path
import sys
from typing import List

# Configure test environment
TEST_DIR: Path = Path(__file__).parent
ROOT_DIR: Path = TEST_DIR.parent

# Add project root to PYTHONPATH for proper imports during testing
sys.path.insert(0, str(ROOT_DIR))

# Test configuration
TEST_ENV: str = "test"
ALLOWED_TEST_ENVS: List[str] = ["test", "development"]

# Ensure we're in a test environment
assert os.getenv("ENVIRONMENT", TEST_ENV) in ALLOWED_TEST_ENVS, (
    "Tests must be run in a test environment. "
    "Set ENVIRONMENT=test in your .env file or environment variables."
)