from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.profiles import router as profiles_router
from app.routers.search import router as search_router

app = FastAPI(title="100X Discovery Platform API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(profiles_router, prefix="/api/profiles", tags=["profiles"])
app.include_router(search_router, prefix="/api/search", tags=["search"])

@app.get("/")
async def root():
    return {"message": "Welcome to 100X Discovery Platform API"} 
