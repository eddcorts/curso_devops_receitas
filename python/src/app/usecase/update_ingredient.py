from pydantic import BaseModel

from ..data_source.ingredient_data_source import IngredientDataSource
from ..entity.ingredient import IngredientID, StandardIngredientUnitsType


class UpdateIngredient(BaseModel):
    """Update one ingredient"""

    ingredient_data_source: IngredientDataSource

    def execute(
        self,
        id: IngredientID,
        new_name: IngredientID | None,
        new_unit: StandardIngredientUnitsType | None,
    ) -> None:
        """Run main class purpose"""
        if new_name is None and new_unit is None:
            raise ValueError("At least one field should be supplied")

        return self.ingredient_data_source.update_ingredient(id, new_name, new_unit)
