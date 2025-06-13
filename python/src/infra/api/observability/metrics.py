import time

from fastapi import Request
from prometheus_client import Counter, Histogram, make_asgi_app
from starlette.middleware.base import RequestResponseEndpoint
from starlette.routing import BaseRoute, Match

# Prometheus
metrics_labels = ["method", "route", "status_code"]

REQUEST_DURATION = Histogram(
    "fastapi_http_request_duration_seconds",
    "Request duration in seconds",
    metrics_labels,
)
REQUEST_COUNT = Counter(
    "fastapi_http_requests_count",
    "Total HTTP requests",
    metrics_labels,
)


async def monitor_requests_middleware(
    request: Request, call_next: RequestResponseEndpoint
):
    """Measure the metrics for prometheus for each request"""
    # Identify endpoint route pattern
    route = None
    app_route: BaseRoute
    for app_route in request.app.routes:
        match, _ = app_route.matches(request.scope)
        if match == Match.FULL:
            route = app_route.path  # type: ignore
            break

    if not route:
        route = request.url.path

    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    # Record metrics
    REQUEST_DURATION.labels(
        method=request.method,
        route=route,
        status_code=response.status_code,
    ).observe(process_time)

    REQUEST_COUNT.labels(
        method=request.method,
        route=route,
        status_code=response.status_code,
    ).inc()

    return response


metrics_app = make_asgi_app()
