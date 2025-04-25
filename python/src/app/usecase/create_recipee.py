from pydantic import BaseModel

from ..data_source.recipee_data_source import RecipeeDataSource
from ..entity.ingredient import Ingredient, IngredientID
from ..entity.recipee import Recipee, RecipeeID


class CreateRecipee(BaseModel):
    """Create one recipee"""

    recipee_data_source: RecipeeDataSource

    def execute(
        self,
        recipee: Recipee,
        existing_ingredients: set[Ingredient],
    ) -> RecipeeID:
        """Run main class purpose"""
        existing_ingredients_ids = {
            ingredient.name for ingredient in existing_ingredients
        }

        possibly_not_existing_ids = set(
            new_ingredient.name for new_ingredient in (recipee.ingredients or set())
        ).difference(existing_ingredients_ids)
        if len(possibly_not_existing_ids) > 0:
            raise ValueError(
                f"Some ingredients IDs passed don't exist: {possibly_not_existing_ids}"
            )

        return self.recipee_data_source.create_recipee(recipee)
