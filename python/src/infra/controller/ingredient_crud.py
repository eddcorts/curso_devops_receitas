from ...app.entity.ingredient import Ingredient, IngredientID
from ...app.usecase.create_ingredient import CreateIngredient
from ...app.usecase.read_ingredients import ReadIngredients
from ..data_source.ingredient_local_data_source import IngredientLocalDataSource

ingredient_local_data_source = IngredientLocalDataSource()


class IngredientCRUD:
    """Methods for creating, reading, updating and deleting ingredients"""

    @staticmethod
    async def create_ingredient(ingredient: Ingredient) -> IngredientID:
        create_ingredient = CreateIngredient(
            ingredient_data_source=ingredient_local_data_source
        )

        return create_ingredient.execute(ingredient)

    @staticmethod
    async def read_ingredients(ids: set[str]) -> set[Ingredient]:
        read_ingredients = ReadIngredients(
            ingredient_data_source=ingredient_local_data_source
        )

        return read_ingredients.execute(ids)
