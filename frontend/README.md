# Frontend

## Quickstart (local)
```bash
cd frontend
python -m http.server 3000
```

Open http://localhost:3000 in your browser and click "Load data".

If your backend runs on a different host or port, update `API_BASE_URL` in `config.js` (local) or set `API_BASE_URL` when running the Docker container.

## Run with Docker (nginx)
```bash
docker build -t ch1-frontend .
docker run --rm --name ch1-frontend --network ch1-net -p 3000:80 -e API_BASE_URL= ch1-frontend
```

Open http://localhost:3000 and click "Load data".

Notes:
- This container proxies `/api/*` to `http://ch1-backend:8080`, so run the backend with `--name ch1-backend` on the same Docker network.
