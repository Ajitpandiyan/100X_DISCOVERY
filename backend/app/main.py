"""Main application module for the FastAPI backend."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routers import profiles, search

app = FastAPI(
    title="100X Discovery API",
    description="Backend API for 100X Discovery Platform",
    version="1.0.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(
    profiles.router,
    prefix="/api/v1/profiles",
    tags=["profiles"],
)
app.include_router(
    search.router,
    prefix="/api/v1/search",
    tags=["search"],
)

@app.get("/health")
async def root() -> dict[str, str]:
    """Root health check endpoint.

    Returns:
        dict[str, str]: Health status response
    """
    return {"status": "healthy", "service": "100X Discovery API"}