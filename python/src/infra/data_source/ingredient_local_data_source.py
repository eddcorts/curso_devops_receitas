from ...app.data_source.ingredient_data_source import IngredientDataSource
from ...app.entity.ingredient import (
    Ingredient,
    IngredientID,
    StandardIngredientUnitsType,
)
from ...app.errors.custom_error import (
    IdentifierAlreadyExistsError,
    IdentifierNotFoundError,
)


class IngredientLocalDataSource(IngredientDataSource):

    ingredients: set[Ingredient] = set()

    def read_ingredients(self, ids: set[IngredientID]) -> set[Ingredient]:
        """Get ingredients with given ID. If no ID is provided, then get all ingredients."""
        if len(ids) == 0:
            return self.ingredients

        return {ingredient for ingredient in self.ingredients if ingredient.name in ids}

    def create_ingredient(self, ingredient: Ingredient) -> IngredientID:
        if ingredient.name in (ingredient.name for ingredient in self.ingredients):
            raise IdentifierAlreadyExistsError(
                f'Ingredient with name "{ingredient.name}" already exists.'
            )

        self.ingredients.add(ingredient)
        return ingredient.name

    def update_ingredient(
        self,
        id: IngredientID,
        new_name: IngredientID | None,
        new_unit: StandardIngredientUnitsType | None,
    ) -> None:
        # TODO: deal with Nones
        try:
            current_ingredient = self.read_ingredients(
                {
                    id,
                }
            ).pop()
        except KeyError:
            raise IdentifierNotFoundError(f"No ingredients found with given ID {id}")

        self.delete_ingredients(
            {
                id,
            }
        )
        self.create_ingredient(
            Ingredient(
                name=new_name or current_ingredient.name,
                standard_unit=new_unit or current_ingredient.standard_unit,
            )
        )

    def delete_ingredients(self, ids: set[IngredientID]) -> set[IngredientID]:
        ingredients = self.read_ingredients(ids)

        if len(ingredients) == 0:
            raise IdentifierNotFoundError(f"No ingredients found with given IDs {ids}")

        self.ingredients -= ingredients

        return {ingredient.name for ingredient in ingredients}
