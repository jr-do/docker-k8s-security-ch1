from __future__ import annotations

from datetime import datetime, timezone
import json
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="fastapi-backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root() -> dict[str, str]:
    return {"name": "fastapi-backend"}


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/info")
def api_info() -> dict[str, Any]:
    timestamp = datetime.now(timezone.utc).isoformat()
    public_ip = "public IP not available"
    ip_location: dict[str, Any] | None = None
    try:
        with urlopen("https://api.ipify.org?format=json", timeout=2) as response:
            data = json.loads(response.read().decode("utf-8"))
            public_ip = data.get("ip", public_ip)
    except (URLError, HTTPError, TimeoutError, json.JSONDecodeError):
        pass
    if public_ip != "public IP not available":
        try:
            with urlopen(f"https://ipwho.is/{public_ip}?output=json", timeout=2) as response:
                geo = json.loads(response.read().decode("utf-8"))
                if geo.get("success", True) is True:
                    ip_location = {
                        "country": geo.get("country"),
                        "region": geo.get("region"),
                        "city": geo.get("city"),
                        "lat": geo.get("latitude"),
                        "lon": geo.get("longitude"),
                        "asn": geo.get("connection", {}).get("asn"),
                        "org": geo.get("connection", {}).get("org"),
                    }
        except (URLError, HTTPError, TimeoutError, json.JSONDecodeError):
            pass
    return {
        "service": "backend",
        "version": "1.0.0",
        "timestamp": timestamp,
        "message": "Hello from the API",
        "items": ["docker", "kubernetes", "security"],
        "public_ip": public_ip,
        "ip_location": ip_location,
    }
