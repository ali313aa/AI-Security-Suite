# Architecture

This project uses a modular three-layer architecture:

1. AI Layer
   - Generates code and explanations
   - Helps reason about tasks and plans

2. Security Layer
   - Scans code for common patterns of risk
   - Produces structured findings with severity levels

3. API/UI Layer
   - Exposes REST endpoints for integration
   - Provides a lightweight browser dashboard

## Current modules

- `app.core.ai_agent`: code generation helper
- `app.core.security`: security scanner
- `app.core.health`: health and status service
- `app.routers.health`: API endpoints for generation and analysis
- `frontend/index.html`: browser-based UI

## Planned extensions

- Git repository scanning
- Better vulnerability detection
- Authentication and authorization
- AI recommendation engine
- Report export and analytics
- Support for multiple AI providers
