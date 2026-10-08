# Architecture

This project is designed as a modular, extensible platform built around three layers:

1. AI Layer
   - Generates code based on user prompts
   - Explains code behavior and risk areas
   - Can optionally connect to an OpenAI-compatible API if an API key is set

2. Security Layer
   - Detects common vulnerable patterns such as SQL injection, secrets, shell execution, eval, and unsafe deserialization
   - Assigns risk levels and summarizes findings

3. Application Layer
   - Exposes REST endpoints for automation and frontend integration
   - Provides a small dashboard for local testing and demonstration

## Current implementation

The repository now contains:
- FastAPI web service
- AI code generation helpers
- Security scanner with risk scoring
- Planning and report modules
- Browser-based dashboard for testing functionality

## API overview

- `GET /health` : basic service health
- `GET /api/status` : module and service status
- `POST /api/generate` : generate code from a task description
- `POST /api/analyze` : scan source code and explain it
- `POST /api/plan` : create an execution plan for a goal
- `POST /api/scan` : scan code and return structured findings

## Security execution model

The scanner checks for common code patterns and returns structured output with:
- category
- severity
- pattern
- message
- line number
- summary and risk score

## Future enhancement roadmap

- Add authentication and user management
- Add Git repository scanning
- Add support for multiple AI providers
- Export reports as HTML/PDF
- Add integration with CI/CD and code review pipelines
