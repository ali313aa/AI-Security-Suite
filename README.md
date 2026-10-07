# AI Security Suite

AI Security Suite is an AI-powered security and code assistant platform. It provides:
- AI-powered code generation and explanation
- Static vulnerability detection for common security issues
- FastAPI backend for automation and integration
- Minimal frontend dashboard for live demos
- Extensible architecture for future integrations

## Features

- Generate code from natural-language prompts
- Analyze code for risky patterns such as SQL injection, secrets, unsafe eval, and shell execution
- Expose API endpoints for integration with web apps and automation tools
- Provide a simple dashboard UI
- Ready for future enhancements like auth, repo scanning, and AI model integration

## Tech stack

- Backend: Python + FastAPI
- Frontend: HTML + JavaScript
- Security analysis: static heuristic scanning
- AI layer: prompt-based generation and explanation helpers

## Run locally

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Then open:
- API docs: http://localhost:8000/docs
- Frontend: `frontend/index.html`

## Project layout

```text
AI-Security-Suite/
├── backend/
│   ├── app/
│   │   ├── core/
│   │   ├── routers/
│   │   ├── config.py
│   │   ├── main.py
│   │   └── __init__.py
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   └── index.html
├── docs/
│   └── ARCHITECTURE.md
├── .gitignore
├── docker-compose.yml
├── requirements.txt
├── README.md
└── LICENSE
```

## Roadmap

- [ ] Add user authentication and authorization
- [ ] Add repository scanning from GitHub and local files
- [ ] Add AI-driven fix suggestions
- [ ] Add report export and logs
- [ ] Add CI/CD and deployment integration
- [ ] Add support for multiple AI models

## License

MIT
