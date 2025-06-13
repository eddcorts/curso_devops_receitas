from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from ...app.errors.custom_error import CustomError


def add_error_handlers(app: FastAPI) -> None:
    """Create Error Handlers for Fast API"""

    @app.exception_handler(CustomError)
    async def handler(_: Request, exc: CustomError) -> JSONResponse:
        """Exception handler"""
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": f"Oops! {exc.detail}"},
        )
