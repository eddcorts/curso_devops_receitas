from fastapi import FastAPI, Query

from ...app.entity.ingredient import (
    Ingredient,
    IngredientID,
)
from ..controller.ingredient_crud import IngredientCRUD

app = FastAPI(
    title="Ingredientes e Receitas",
)


app.post("/ingredient/create/", tags=["Ingredient"])(IngredientCRUD.create_ingredient)


@app.get("/ingredient/read/", tags=["Ingredient"])  # (IngredientCRUD.read_ingredients)
async def read_ingredients(
    ids: set[IngredientID] = Query(set()),
) -> set[Ingredient]:
    return await IngredientCRUD.read_ingredients(ids)
