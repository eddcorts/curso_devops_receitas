from fastapi import FastAPI

from ..controller.ingredient_crud import IngredientCRUD
from ..controller.recipee_crud import RecipeeCRUD

app = FastAPI(title="Ingredientes e Receitas", root_path="/python")


@app.get("/health")
async def health() -> bool:
    return True


app.post("/ingredient/create", tags=["Ingredient"])(IngredientCRUD.create_ingredient)


app.get("/ingredient/read", tags=["Ingredient"])(IngredientCRUD.read_ingredients)

app.delete("/ingredient/delete", tags=["Ingredient"])(IngredientCRUD.delete_ingredients)

app.put("/ingredients/update", tags=["Ingredient"])(IngredientCRUD.update_ingredient)


app.post("/recipee/create", tags=["Recipee"])(RecipeeCRUD.create_recipee)
app.get("/recipee/read", tags=["Recipee"])(RecipeeCRUD.read_recipees)
app.delete("/recipee/delete", tags=["Recipee"])(RecipeeCRUD.delete_recipees)
app.put("/recipees/update", tags=["Recipee"])(RecipeeCRUD.update_recipee)
app.put("/recipees/update/recipee", tags=["Recipee"])(
    RecipeeCRUD.update_recipee_ingredient
)
