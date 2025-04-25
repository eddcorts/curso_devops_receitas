# checar caso de parametro vazio
from pydantic import BaseModel

from ..data_source.ingredient_data_source import IngredientDataSource
from ..entity.ingredient import IngredientID


class DeleteIngredients(BaseModel):
    """Delete one or more ingredients"""

    ingredient_data_source: IngredientDataSource

    def execute(self, ids: set[IngredientID]) -> set[IngredientID]:
        """Run main class purpose"""
        return self.ingredient_data_source.delete_ingredients(ids)
