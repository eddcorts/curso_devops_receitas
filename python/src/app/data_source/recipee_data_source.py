from abc import ABC, abstractmethod

from pydantic import BaseModel

from ..entity.ingredient import IngredientID, StandardIngredientUnitsType
from ..entity.recipee import TIME_UNIT_TYPE, Recipee, RecipeeID, RecipeeIngredient


class RecipeeDataSource(ABC, BaseModel):
    """Abstract class for each use case that works with recipees"""

    recipees: list[Recipee]

    @abstractmethod
    def get_recipees(self, ids: set[RecipeeID]) -> list[Recipee]:
        """Get recipees with given ID. If no ID is provided, then get all recipees."""

    @abstractmethod
    def create_recipee(self, recipee: Recipee) -> RecipeeID: ...

    @abstractmethod
    def update_recipee(
        self,
        id: RecipeeID,
        new_name: RecipeeID | None,
        new_time: float | None,
        new_time_unit: TIME_UNIT_TYPE | None,
        new_steps: str | None,
        new_ingredients: set[RecipeeIngredient],
        remove_ingredients: set[IngredientID],
    ) -> None: ...

    @abstractmethod
    def update_recipee_ingredient(
        self,
        recipee_id: RecipeeID,
        ingredient_id: IngredientID,
        new_specification: str | None,
        new_quantity: float | None,
        new_override_unit: StandardIngredientUnitsType | None,
    ) -> None: ...

    @abstractmethod
    def delete_recipees(self, ids: set[RecipeeID]) -> set[RecipeeID]: ...
