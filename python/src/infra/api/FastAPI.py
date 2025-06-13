from fastapi import Body, FastAPI, Query

from ...app.entity.ingredient import (
    Ingredient,
    IngredientID,
    StandardIngredientUnitsType,
)
from ...app.entity.recipee import TIME_UNIT_TYPE, Recipee, RecipeeID, RecipeeIngredient
from ..controller.ingredient_crud import IngredientCRUD
from ..controller.recipee_crud import RecipeeCRUD
from .FastAPIErrorHandler import add_error_handlers
from .observability import apply_observability_on_app

app = FastAPI(title="Ingredientes e Receitas", root_path="/python")

add_error_handlers(app)
apply_observability_on_app(app)


@app.get("/health")
async def health() -> bool:
    return True


app.post("/ingredient/create", tags=["Ingredient"])(IngredientCRUD.create_ingredient)


@app.get("/ingredient/read", tags=["Ingredient"])
async def read_ingredients(
    ids: set[IngredientID] | None = Query(None),
) -> set[Ingredient]:
    return await IngredientCRUD.read_ingredients(ids)


app.delete("/ingredient/delete", tags=["Ingredient"])(IngredientCRUD.delete_ingredients)
app.put("/ingredients/update", tags=["Ingredient"])(IngredientCRUD.update_ingredient)


app.post("/recipee/create", tags=["Recipee"])(RecipeeCRUD.create_recipee)


@app.get("/recipee/read", tags=["Recipee"])
async def read_recipees(
    ids: set[RecipeeID] | None = Query(None),
) -> list[Recipee]:
    return await RecipeeCRUD.read_recipees(ids)


app.delete("/recipee/delete", tags=["Recipee"])(RecipeeCRUD.delete_recipees)


@app.put("/recipees/update", tags=["Recipee"])
async def update_recipee(
    id: RecipeeID = Body(),
    new_name: RecipeeID | None = Body(None),
    new_time: float | None = Body(None),
    new_time_unit: TIME_UNIT_TYPE | None = Body(None),
    new_steps: str | None = Body(None),
    new_ingredients: set[RecipeeIngredient] | None = Body(None),
    remove_ingredients: set[IngredientID] | None = Body(None),
) -> None:
    return await RecipeeCRUD.update_recipee(
        id,
        new_name,
        new_time,
        new_time_unit,
        new_steps,
        new_ingredients,
        remove_ingredients,
    )


@app.put("/recipees/update/recipee", tags=["Recipee"])
async def update_recipee_ingredient(
    recipee_id: RecipeeID = Body(),
    ingredient_id: IngredientID = Body(),
    new_specification: str | None = Body(None),
    new_quantity: float | None = Body(None),
    new_override_unit: StandardIngredientUnitsType | None = Body(None),
) -> None:
    return await RecipeeCRUD.update_recipee_ingredient(
        recipee_id, ingredient_id, new_specification, new_quantity, new_override_unit
    )
