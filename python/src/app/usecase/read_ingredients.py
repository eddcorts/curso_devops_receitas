from pydantic import BaseModel

from ..data_source.ingredient_data_source import IngredientDataSource
from ..entity.ingredient import Ingredient, IngredientID


class ReadIngredients(BaseModel):
    """Read one or more ingredients"""

    ingredient_data_source: IngredientDataSource

    def execute(self, ids: set[IngredientID] | None = None) -> set[Ingredient]:
        """Run main class purpose"""
        return self.ingredient_data_source.read_ingredients(ids or set())
