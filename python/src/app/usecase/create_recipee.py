from pydantic import BaseModel

from ..data_source.recipee_data_source import RecipeeDataSource
from ..entity.ingredient import Ingredient
from ..entity.recipee import Recipee, RecipeeID
from ..errors.custom_error import IdentifierNotFoundError


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

        possibly_not_existing_ids = {
            new_ingredient.ingredient_id for new_ingredient in recipee.ingredients
        }.difference(existing_ingredients_ids)
        if len(possibly_not_existing_ids) > 0:
            raise IdentifierNotFoundError(
                f"Some ingredients IDs passed don't exist: {possibly_not_existing_ids}"
            )

        return self.recipee_data_source.create_recipee(recipee)
