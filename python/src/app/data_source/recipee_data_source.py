from abc import ABC, abstractmethod

from ..entity.recipee import Recipee


class RecipeeDataSource(ABC):
    """Abstract class for each use case that works with recipees"""

    recipees: set[Recipee]

    @abstractmethod
    def get_recipees(self, ids: set[int]) -> set[Recipee]:
        """Get recipees with given ID. If no ID is provided, then get all recipees."""

    @abstractmethod
    def create_recipee(self, recipee: Recipee) -> int: ...

    @abstractmethod
    def update_recipee(self, id: int, updated_recipee: Recipee) -> None: ...

    @abstractmethod
    def delete_recipees(self, ids: set[int]) -> None: ...
