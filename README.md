# Chapter 1 Exercise: FastAPI backend + simple frontend

## Prereqs
- Python 3.11+
- pip (or uv)

## Run the backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
PORT=8080 uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
```

Notes:
- The backend uses port 8080 by default. To change it, set `PORT` and pass the same value to `--port`.

## Run the frontend
```bash
cd frontend
python -m http.server 3000
```

Open http://localhost:3000 and click "Load data".

## Test the API with curl
```bash
curl http://localhost:8080/
curl http://localhost:8080/healthz
curl http://localhost:8080/api/info
```
