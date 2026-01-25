# Backend (FastAPI)

## Prereqs
- Python 3.11+

## Setup
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
```

## Run (local)
```bash
cd backend
source .venv/bin/activate
PORT=8080 uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
```

Notes:
- The backend uses port 8080 by default. To change it, set `PORT` and pass the same value to `--port`.

## Run with Docker
```bash
docker build -t ch1-backend .
docker run --rm -p 8080:8080 -e PORT=8080 ch1-backend
```

## Test
```bash
curl http://localhost:8080/healthz
curl http://localhost:8080/api/info
```
