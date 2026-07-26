from fastapi import FastAPI

from app.config.settings import settings
from app.router.complaint import router as complaint_router

app = FastAPI(
    title=settings.APP_NAME,
    # description="AI-powered complaint management system for pharmaceutical manufacturing.",
    version=settings.APP_VERSION
)

app.include_router(complaint_router)

@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.APP_NAME}"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }