# Frontend

## Quickstart (local)
```bash
cd frontend
python -m http.server 3000
```

Open http://localhost:3000 in your browser and click "Load data".

If your backend runs on a different host or port, update `API_BASE_URL` in `index.html`.

## Run with Docker (nginx)
```bash
docker build -t ch1-frontend .
docker run --rm -p 3000:80 ch1-frontend
```

Open http://localhost:3000 and click "Load data".
