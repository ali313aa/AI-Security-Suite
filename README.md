# AI Security Suite

AI Security Suite is a full-stack AI-assisted application focused on secure code generation, vulnerability analysis, and developer productivity.

## Features

- AI-assisted code generation from natural language
- Static security scanning for common cybersecurity risks
- Risk scoring and severity classification
- Simple planning engine for task execution
- FastAPI backend with REST endpoints
- Lightweight frontend dashboard for interaction
- Optional OpenAI API integration when an API key is configured

## Stack

- Backend: Python, FastAPI
- Frontend: HTML, CSS, JavaScript
- AI layer: prompt-based generation with optional OpenAI integration
- Security analysis: static pattern detection and scoring

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

Open:
- API docs: http://localhost:8000/docs
- Frontend: frontend/index.html

## Environment Variables

```bash
cp .env.example .env
```

Add optional values:

```env
OPENAI_API_KEY=your_api_key_here
DEBUG=true
```

## Main API Endpoints

- `GET /health`
- `GET /api/status`
- `POST /api/generate`
- `POST /api/analyze`
- `POST /api/plan`
- `POST /api/scan`

## Project Structure

```text
AI-Security-Suite/
├── backend/
│   ├── app/
│   │   ├── core/
│   │   │   ├── ai_agent.py
│   │   │   ├── health.py
│   │   │   ├── planner.py
│   │   │   ├── risk_report.py
│   │   │   └── security.py
│   │   ├── routers/
│   │   │   └── health.py
│   │   ├── config.py
│   │   ├── main.py
│   │   └── __init__.py
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   └── index.html
├── docs/
│   └── ARCHITECTURE.md
├── .env.example
├── .gitignore
├── README.md
├── docker-compose.yml
├── requirements.txt
├── LICENSE
└──
```

## Security Note

This project is a security-focused toolkit for analysis and development assistance. It is designed for educational, internal, and secure engineering workflows. Always validate findings manually before using them in production systems.

## License

MIT
