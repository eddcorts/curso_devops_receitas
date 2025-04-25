from ...app.entity.ingredient import (
    Ingredient,
    IngredientID,
    StandardIngredientUnitsType,
)
from ...app.usecase.create_ingredient import CreateIngredient
from ...app.usecase.delete_ingredients import DeleteIngredients
from ...app.usecase.read_ingredients import ReadIngredients
from ...app.usecase.update_ingredient import UpdateIngredient
from . import ingredient_data_source


class IngredientCRUD:
    """Methods for creating, reading, updating and deleting ingredients"""

    @staticmethod
    async def create_ingredient(ingredient: Ingredient) -> IngredientID:
        create_ingredient = CreateIngredient(
            ingredient_data_source=ingredient_data_source
        )

        return create_ingredient.execute(ingredient)

    @staticmethod
    async def read_ingredients(ids: set[IngredientID] | None = None) -> set[Ingredient]:
        read_ingredients = ReadIngredients(
            ingredient_data_source=ingredient_data_source
        )

        return read_ingredients.execute(ids)

    @staticmethod
    async def delete_ingredients(ids: set[IngredientID]) -> set[IngredientID]:
        delete_ingredients = DeleteIngredients(
            ingredient_data_source=ingredient_data_source
        )

        return delete_ingredients.execute(ids)

    @staticmethod
    async def update_ingredient(
        id: IngredientID,
        new_name: IngredientID | None = None,
        new_unit: StandardIngredientUnitsType | None = None,
    ) -> None:
        update_ingredient = UpdateIngredient(
            ingredient_data_source=ingredient_data_source
        )

        return update_ingredient.execute(id, new_name, new_unit)
