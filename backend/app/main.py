from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers.health import router as health_router

app = FastAPI(
    title=settings.app_name,
    version=settings.api_version,
    description="AI Security Suite API for code generation and static security analysis",
    debug=settings.debug,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.app_name}",
        "environment": settings.environment,
    }


@app.get("/health")
def health():
    return {"status": "ok", "service": settings.app_name}
