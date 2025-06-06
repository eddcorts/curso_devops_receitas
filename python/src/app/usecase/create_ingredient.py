from pydantic import BaseModel

from ..data_source.ingredient_data_source import IngredientDataSource
from ..entity.ingredient import Ingredient, IngredientID


class CreateIngredient(BaseModel):
    """Create one ingredient"""

    ingredient_data_source: IngredientDataSource

    def execute(self, ingredient: Ingredient) -> IngredientID:
        """Run main class purpose"""
        return self.ingredient_data_source.create_ingredient(ingredient)
