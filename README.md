# Chapter 1 Exercise: FastAPI backend + simple frontend

## Prereqs
- Python 3.11+
- pip (or uv)
- Docker (optional, for containerized run)

## Run the backend (local)
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

## Run the frontend (local)
```bash
cd frontend
python -m http.server 3000
```

Open http://localhost:3000 and click "Load data".

## Run with Docker

Create a shared network:
```bash
docker network create ch1-net
```

Backend:
```bash
docker build -t ch1-backend ./backend
docker run --rm --name ch1-backend --network ch1-net -p 8080:8080 -e PORT=8080 ch1-backend
```

Frontend (nginx):
```bash
docker build -t ch1-frontend ./frontend
docker run --rm --name ch1-frontend --network ch1-net -p 3000:80 -e API_BASE_URL= ch1-frontend
```

Open http://localhost:3000 and click "Load data".

Notes:
- The nginx frontend proxies `/api/*` to `http://ch1-backend:8080` on the Docker network.
- For local (non-Docker) frontend, edit `frontend/config.js` to point at your backend.

## Test the API with curl
```bash
curl http://localhost:8080/
curl http://localhost:8080/healthz
curl http://localhost:8080/api/info
```
