from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.core.ai_agent import AIAgent
from app.core.health import HealthService
from app.core.planner import Planner
from app.core.risk_report import RiskReporter
from app.core.security import SecurityScanner

router = APIRouter(prefix="/api")

ai_agent = AIAgent()
health_service = HealthService()
planner = Planner()
security_scanner = SecurityScanner()
risk_reporter = RiskReporter()


class CodeRequest(BaseModel):
    task: str
    language: str = "python"


class CodeAnalysisRequest(BaseModel):
    code: str
    filename: str = "snippet.py"


class GoalRequest(BaseModel):
    goal: str


@router.get("/status")
def get_status():
    return health_service.get_status()


@router.get("/health")
def get_api_health():
    return {"status": "ok", "service": "AI Security Suite API"}


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
    scan = security_scanner.scan(request.code, request.filename)
    explanation = ai_agent.explain(request.code)
    return {
        "scan": scan,
        "explanation": explanation,
        "report": risk_reporter.build_report(scan["findings"]),
    }


@router.post("/plan")
def create_plan(request: GoalRequest):
    if not request.goal:
        raise HTTPException(status_code=400, detail="Goal is required.")
    return {"plan": planner.plan(request.goal)}


@router.post("/scan")
def scan_code(request: CodeAnalysisRequest):
    if not request.code:
        raise HTTPException(status_code=400, detail="Code is required.")
    return security_scanner.scan(request.code, request.filename)
