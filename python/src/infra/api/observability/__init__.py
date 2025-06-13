from fastapi import FastAPI

from .metrics import metrics_app, monitor_requests_middleware


def apply_observability_on_app(app: FastAPI) -> None:
    """Insert into the app the observability plugins"""
    # importing .logs already apply the log collection
    from .logs import uvicorn_access_logger  # type: ignore

    app.mount("/metrics", metrics_app)
    app.middleware("http")(monitor_requests_middleware)
