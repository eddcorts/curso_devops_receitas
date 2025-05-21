from ...app.entity.ingredient import IngredientID, StandardIngredientUnitsType
from ...app.entity.recipee import (
    TIME_UNIT_TYPE,
    Recipee,
    RecipeeID,
    RecipeeIngredient,
)
from ...app.usecase.create_recipee import CreateRecipee
from ...app.usecase.delete_recipees import DeleteRecipees
from ...app.usecase.read_ingredients import ReadIngredients
from ...app.usecase.read_recipees import ReadRecipees
from ...app.usecase.update_recipee import UpdateRecipee
from ...app.usecase.update_recipee_ingredient import UpdateRecipeeIngredient
from . import ingredient_data_source, recipee_data_source


class RecipeeCRUD:
    """Methods for creating, reading, updating and deleting recipees"""

    @staticmethod
    async def create_recipee(recipee: Recipee) -> RecipeeID:
        read_ingredients = ReadIngredients(
            ingredient_data_source=ingredient_data_source
        )

        create_recipee = CreateRecipee(recipee_data_source=recipee_data_source)

        return create_recipee.execute(recipee, read_ingredients.execute())

    @staticmethod
    async def read_recipees(ids: set[RecipeeID] | None = None) -> list[Recipee]:
        read_recipees = ReadRecipees(recipee_data_source=recipee_data_source)

        return read_recipees.execute(ids)

    @staticmethod
    async def delete_recipees(ids: set[RecipeeID]) -> set[RecipeeID]:
        delete_recipees = DeleteRecipees(recipee_data_source=recipee_data_source)

        return delete_recipees.execute(ids)

    @staticmethod
    async def update_recipee(
        id: RecipeeID,
        new_name: RecipeeID | None = None,
        new_time: float | None = None,
        new_time_unit: TIME_UNIT_TYPE | None = None,
        new_steps: str | None = None,
        new_ingredients: set[RecipeeIngredient] | None = None,
        remove_ingredients: set[IngredientID] | None = None,
    ) -> None:
        read_ingredients = ReadIngredients(
            ingredient_data_source=ingredient_data_source
        )

        update_recipee = UpdateRecipee(recipee_data_source=recipee_data_source)

        return update_recipee.execute(
            id,
            new_name,
            new_time,
            new_time_unit,
            new_steps,
            new_ingredients,
            remove_ingredients,
            read_ingredients.execute(),
        )

    @staticmethod
    async def update_recipee_ingredient(
        recipee_id: RecipeeID,
        ingredient_id: IngredientID,
        new_specification: str | None = None,
        new_quantity: float | None = None,
        new_override_unit: StandardIngredientUnitsType | None = None,
    ) -> None:
        update_recipee = UpdateRecipeeIngredient(
            recipee_data_source=recipee_data_source
        )

        return update_recipee.execute(
            recipee_id,
            ingredient_id,
            new_specification,
            new_quantity,
            new_override_unit,
        )
