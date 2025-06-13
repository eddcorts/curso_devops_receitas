from abc import ABC


class CustomError(ABC, Exception):
    """Base Error class for others to inherit."""

    detail: str
    status_code: int


class IdentifierAlreadyExistsError(CustomError):
    """Entity with given identifier already exists"""

    detail = "Entity with this name already exists."
    status_code = 409


class IdentifierNotFoundError(CustomError):
    """No entities found with given identifier(s)"""

    detail = "No entities found with given ID"
    status_code = 404

    def __init__(self, detail: str | None = None):
        self.detail = detail or self.detail
