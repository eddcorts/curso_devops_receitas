from abc import ABC, abstractmethod

from pydantic import BaseModel

from ..entity.ingredient import Ingredient, IngredientID, StandardIngredientUnitsType


class IngredientDataSource(ABC, BaseModel):
    """Abstract class for each use case that works with ingredients"""

    ingredients: set[Ingredient]

    @abstractmethod
    def read_ingredients(self, ids: set[IngredientID]) -> set[Ingredient]:
        """Get ingredients with given ID. If no ID is provided, then get all ingredients."""

    @abstractmethod
    def create_ingredient(self, ingredient: Ingredient) -> IngredientID: ...

    @abstractmethod
    def update_ingredient(
        self,
        id: IngredientID,
        new_name: IngredientID | None,
        new_unit: StandardIngredientUnitsType | None,
    ) -> None: ...

    @abstractmethod
    def delete_ingredients(self, ids: set[IngredientID]) -> set[IngredientID]: ...
