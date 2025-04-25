from pydantic import BaseModel

from ..data_source.recipee_data_source import RecipeeDataSource
from ..entity.ingredient import IngredientID, StandardIngredientUnitsType
from ..entity.recipee import RecipeeID


class UpdateRecipeeIngredient(BaseModel):
    """Update one ingredient from a recipee"""

    recipee_data_source: RecipeeDataSource

    def execute(
        self,
        recipee_id: RecipeeID,
        ingredient_id: IngredientID,
        new_specification: str | None,
        new_quantity: float | None,
        new_override_unit: StandardIngredientUnitsType | None,
    ) -> None:
        """Run main class purpose"""
        if (
            new_specification is None
            and new_quantity is None
            and new_override_unit is None
        ):
            raise ValueError("At least one field should be supplied")

        return self.recipee_data_source.update_recipee_ingredient(
            recipee_id,
            ingredient_id,
            new_specification,
            new_quantity,
            new_override_unit,
        )
