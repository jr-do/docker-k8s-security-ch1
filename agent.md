# Agent Instructions (Codex)

## Goal
Create a GitHub repo with:
1) Backend: FastAPI REST API that returns a JSON object.
2) Frontend: simple HTML page that fetches the JSON and displays it.

## Constraints
- Minimal, beginner-friendly.
- No database.
- Must run locally on macOS/Linux.
- Backend must allow browser calls (CORS).
- Provide clear run instructions in root README.

## Tech Choices
- Backend: Python 3.11+ with FastAPI + Uvicorn
- Frontend: plain HTML + JavaScript

## Backend Requirements
- Location: /backend
- Python packaging: use `pyproject.toml` (uv or poetry-style is fine; prefer uv)
- App module: `backend/app/main.py`
- Endpoints:
  - GET `/healthz` -> `{ "status": "ok" }`
  - GET `/api/info` -> JSON object:
    ```json
    {
      "service": "backend",
      "version": "1.0.0",
      "timestamp": "<ISO string>",
      "message": "Hello from the API",
      "items": ["docker", "kubernetes", "security"]
    }
    ```
- Port: 8080 default (configurable via environment variable `PORT`)
- CORS:
  - enable for all origins in development (or at least for http://localhost:3000 / common local origins)
- Add a `GET /` that returns a small message like `{ "name": "fastapi-backend" }` (optional but nice)
- Provide `backend/README.md` with:
  - create venv
  - install deps
  - run server
  - curl examples

## Frontend Requirements
- Location: /frontend
- Single file `index.html` that:
  - Has title + a "Load data" button
  - Shows loading status
  - Fetches from backend endpoint (default: `http://localhost:8080/api/info`)
  - Pretty-prints JSON in a `<pre>` block
  - Handles errors (backend down / wrong URL) with a visible message
- Allow easy configuration:
  - API_BASE_URL constant at the top of the script

## Documentation
- Root `README.md` must include:
  - Prereqs (Python version)
  - How to run backend
  - How to run frontend (use `python -m http.server 3000` recommended)
  - How to test endpoints with curl
- Provide `frontend/README.md` quickstart.

## Deliverables Checklist
- backend/pyproject.toml + pinned-ish dependencies
- backend/app/main.py implemented
- frontend/index.html implemented
- .gitignore
- READMEs
- Everything runs locally with simple commands

## Quality Bar
- Keep it small and readable.
- Use type hints where natural.
- No unnecessary abstractions.

