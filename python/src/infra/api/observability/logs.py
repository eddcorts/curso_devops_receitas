import logging
from multiprocessing import Queue

from logging_loki import LokiQueueHandler  # type: ignore

# Loki
loki_logs_handler = LokiQueueHandler(
    queue=Queue(-1),
    url="http://localhost:3100/loki/api/v1/push",
    tags={"application": "fastapi"},
    version="1",
)

uvicorn_access_logger = logging.getLogger("uvicorn.access")
uvicorn_access_logger.addHandler(loki_logs_handler)


class EndpointFilter(logging.Filter):
    """Filter some logs"""

    def filter(self, record: logging.LogRecord) -> bool:
        """Filter the logs from /metrics endpoint"""
        return record.getMessage().find("GET /metrics") == -1


# Filter out /endpoint
uvicorn_access_logger.addFilter(EndpointFilter())
