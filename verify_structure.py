import os
from pathlib import Path
import sys

required_files = [
    # Root directory
    ".gitignore",
    ".env.example",
    "README.md",
    "docker-compose.yml",
    ".github/workflows/frontend-ci.yml",
    # Frontend
    "frontend/requirements.txt",
    "frontend/streamlit_app.py",
    "frontend/src/components/__init__.py",
    "frontend/src/utils/__init__.py",
    "frontend/src/config.py",
    "frontend/.streamlit/config.toml",
    # Backend
    "backend/requirements.txt",
    "backend/app/main.py",
    "backend/app/routers/__init__.py",
    "backend/app/models/__init__.py",
    "backend/app/services/__init__.py",
    "backend/data/profiles.json",
]


def verify_structure():
    root_dir = Path(__file__).parent
    missing_files = []

    print("Verifying project structure...")
    print("Root directory:", root_dir)
    print("\nChecking required files:")

    for file_path in required_files:
        full_path = root_dir / file_path
        if not full_path.exists():
            missing_files.append(file_path)
            print(f"❌ Missing: {file_path}")
        else:
            print(f"✅ Found: {file_path}")

    if missing_files:
        print(
            "\n⚠️ Missing files found! Please create these files before pushing to GitHub."
        )
        sys.exit(1)
    else:
        print("\n✅ All required files are present!")
        print("\nYou can now commit and push to GitHub:")
        print("git add .")
        print('git commit -m "Initial project setup"')
        print("git push origin main")


if __name__ == "__main__":
    verify_structure()
