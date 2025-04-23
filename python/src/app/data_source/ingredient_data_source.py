from abc import ABC, abstractmethod

from ..entity.ingredient import Ingredient


class IngredientDataSource(ABC):
    """Abstract class for each use case that works with ingredients"""

    ingredients: set[Ingredient]

    @abstractmethod
    def get_ingredients(self, ids: set[int]) -> set[Ingredient]:
        """Get ingredients with given ID. If no ID is provided, then get all ingredients."""

    @abstractmethod
    def create_ingredient(self, ingredient: Ingredient) -> int: ...

    @abstractmethod
    def update_ingredient(self, id: int, updated_ingredient: Ingredient) -> None: ...

    @abstractmethod
    def delete_ingredients(self, ids: set[int]) -> None: ...
