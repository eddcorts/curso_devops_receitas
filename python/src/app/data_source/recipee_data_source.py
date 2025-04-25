from abc import ABC, abstractmethod

from pydantic import BaseModel

from ..entity.recipee import Recipee, RecipeeID


class RecipeeDataSource(ABC, BaseModel):
    """Abstract class for each use case that works with recipees"""

    recipees: set[Recipee]

    @abstractmethod
    def get_recipees(self, ids: set[RecipeeID]) -> set[Recipee]:
        """Get recipees with given ID. If no ID is provided, then get all recipees."""

    @abstractmethod
    def create_recipee(self, recipee: Recipee) -> RecipeeID: ...

    @abstractmethod
    def update_recipee(self, updated_recipee: Recipee) -> None: ...

    @abstractmethod
    def delete_recipees(self, ids: set[RecipeeID]) -> None: ...
