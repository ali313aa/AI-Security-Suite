from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.core.ai_agent import AIAgent
from app.core.health import HealthService
from app.core.security import SecurityScanner

router = APIRouter(prefix="/api")

ai_agent = AIAgent()
security_scanner = SecurityScanner()
health_service = HealthService()


class CodeRequest(BaseModel):
    task: str
    language: str = "python"


class CodeAnalysisRequest(BaseModel):
    code: str


@router.get("/status")
def get_status():
    return health_service.get_status()


@router.post("/generate")
def generate_code(request: CodeRequest):
    if not request.task:
        raise HTTPException(status_code=400, detail="Task is required.")

    result = ai_agent.generate_code(request.task, request.language)
    return {"language": request.language, "code": result}


@router.post("/analyze")
def analyze_code(request: CodeAnalysisRequest):
    if not request.code:
        raise HTTPException(status_code=400, detail="Code is required.")

    scan = security_scanner.scan(request.code)
    explanation = ai_agent.explain(request.code)
    return {"scan": scan, "explanation": explanation}
