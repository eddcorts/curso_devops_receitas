from pydantic import BaseModel

from ..data_source.recipee_data_source import RecipeeDataSource
from ..entity.ingredient import Ingredient, IngredientID
from ..entity.recipee import TIME_UNIT_TYPE, RecipeeID, RecipeeIngredient


class UpdateRecipee(BaseModel):
    """Update one recipee"""

    recipee_data_source: RecipeeDataSource

    def execute(
        self,
        id: RecipeeID,
        new_name: RecipeeID | None,
        new_time: float | None,
        new_time_unit: TIME_UNIT_TYPE | None,
        new_steps: str | None,
        new_ingredients: set[RecipeeIngredient] | None,
        remove_ingredients: set[IngredientID] | None,
        existing_ingredients: set[Ingredient],
    ) -> None:
        """Run main class purpose"""
        if (
            new_name is None
            and new_time is None
            and new_time_unit is None
            and new_steps is None
            and new_ingredients is None
            and remove_ingredients is None
        ):
            raise ValueError("At least one field should be supplied")

        new_ingredients_ids = {
            ingredient.ingredient_id for ingredient in new_ingredients or set()
        }
        if len((remove_ingredients or set()).intersection(new_ingredients_ids)) > 0:
            raise ValueError(
                "Shouldn't remove and add the same ingredient at the same time"
            )

        # TODO: transform into a usecase
        existing_ingredients_ids = {
            ingredient.name for ingredient in existing_ingredients
        }

        possibly_not_existing_ids = new_ingredients_ids.difference(
            existing_ingredients_ids
        )
        if len(possibly_not_existing_ids) > 0:
            raise ValueError(
                f"Some ingredients IDs passed don't exist: {possibly_not_existing_ids}"
            )

        return self.recipee_data_source.update_recipee(
            id,
            new_name,
            new_time,
            new_time_unit,
            new_steps,
            new_ingredients or set(),
            remove_ingredients or set(),
        )
