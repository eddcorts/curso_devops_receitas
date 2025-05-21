from ...app.data_source.recipee_data_source import RecipeeDataSource
from ...app.entity.ingredient import IngredientID, StandardIngredientUnitsType
from ...app.entity.recipee import TIME_UNIT_TYPE, Recipee, RecipeeID, RecipeeIngredient


class RecipeeLocalDataSource(RecipeeDataSource):

    recipees: list[Recipee] = []

    def get_recipees(self, ids: set[RecipeeID]) -> list[Recipee]:
        """Get recipees with given ID. If no ID is provided, then get all recipees."""
        if len(ids) == 0:
            return self.recipees

        return [recipee for recipee in self.recipees if recipee.name in ids]

    def create_recipee(self, recipee: Recipee) -> RecipeeID:
        if recipee.name in (recipee.name for recipee in self.recipees):
            raise ValueError(f'recipee with name "{recipee.name}" already exists.')

        self.recipees.append(recipee)
        return recipee.name

    def update_recipee(
        self,
        id: RecipeeID,
        new_name: RecipeeID | None,
        new_time: float | None,
        new_time_unit: TIME_UNIT_TYPE | None,
        new_steps: str | None,
        new_ingredients: set[RecipeeIngredient],
        remove_ingredients: set[IngredientID],
    ) -> None:

        try:
            current_recipee = next(
                recipee for recipee in self.recipees if recipee.name in id
            )
        except StopIteration:
            raise ValueError(f"No recipees found with given ID {id}")

        updated_ingredients = {
            ingredient
            for ingredient in (current_recipee.ingredients | new_ingredients)
            if ingredient.ingredient_id not in remove_ingredients
        }

        current_recipee_idx = self.recipees.index(current_recipee)

        self.recipees[current_recipee_idx] = Recipee(
            name=new_name or current_recipee.name,
            time=new_time or current_recipee.time,
            time_unit=new_time_unit or current_recipee.time_unit,
            steps=new_steps or current_recipee.steps,
            ingredients=updated_ingredients,
        )

    def update_recipee_ingredient(
        self,
        recipee_id: RecipeeID,
        ingredient_id: IngredientID,
        new_specification: str | None,
        new_quantity: float | None,
        new_override_unit: StandardIngredientUnitsType | None,
    ) -> None:
        # TODO: deal with Nones
        try:
            recipee = self.get_recipees(
                {
                    recipee_id,
                }
            )[0]
        except IndexError:
            raise ValueError(f"No recipee found with given ID {recipee_id}")

        try:
            current_ingredient = next(
                ingredient
                for ingredient in recipee.ingredients
                if ingredient.ingredient_id == ingredient_id
            )
        except StopIteration:
            raise ValueError(
                f"No ingredient found with given ID {ingredient_id} in recipee {recipee_id}"
            )

        current_ingredient.specification = (
            new_specification or current_ingredient.specification
        )
        current_ingredient.quantity = new_quantity or current_ingredient.quantity
        current_ingredient.override_unit = (
            new_override_unit or current_ingredient.override_unit
        )

    def delete_recipees(self, ids: set[RecipeeID]) -> set[RecipeeID]:
        recipees = self.get_recipees(ids)

        if len(recipees) == 0:
            raise ValueError(f"No recipees found with given IDs {ids}")

        recipees_indexes = sorted(
            [self.recipees.index(recipee) for recipee in recipees], reverse=True
        )
        for idx in recipees_indexes:
            self.recipees.pop(idx)

        return {recipee.name for recipee in recipees}
