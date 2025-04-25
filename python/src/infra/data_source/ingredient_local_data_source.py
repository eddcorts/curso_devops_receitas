from ...app.data_source.ingredient_data_source import IngredientDataSource
from ...app.entity.ingredient import Ingredient, IngredientID


class IngredientLocalDataSource(IngredientDataSource):

    ingredients: set[Ingredient] = set()

    def read_ingredients(self, ids: set[IngredientID]) -> set[Ingredient]:
        """Get ingredients with given ID. If no ID is provided, then get all ingredients."""
        if len(ids) == 0:
            return self.ingredients

        return {ingredient for ingredient in self.ingredients if ingredient.name in ids}

    def create_ingredient(self, ingredient: Ingredient) -> IngredientID:
        if ingredient.name in (ingredient.name for ingredient in self.ingredients):
            raise ValueError(
                f'Ingredient with name "{ingredient.name}" already exists.'
            )

        self.ingredients.add(ingredient)
        return ingredient.name

    def update_ingredient(self, updated_ingredient: Ingredient) -> None: ...

    def delete_ingredients(self, ids: set[IngredientID]) -> set[IngredientID]:
        ingredients = self.read_ingredients(ids)

        if len(ingredients) == 0:
            raise ValueError("No ingredients found with given IDs")

        self.ingredients -= ingredients

        return {ingredient.name for ingredient in ingredients}
