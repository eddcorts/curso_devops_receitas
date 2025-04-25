from typing import Literal

from pydantic import Field

from .base import BaseModel

type IngredientID = str
type StandardIngredientUnitsType = Literal[
    "colher de café",
    "colher de sobremesa",
    "colher de chá",
    "colher de sopa",
    "colher de servir",
    "concha",
    "xícara",
    "copo",
    "caixa",
    "lata",
    "mg",
    "g",
    "kg",
    "mL",
    "L",
    "unidade",
    "duzia",
    "a gosto",
] | str


class Ingredient(BaseModel):
    """A ingredient to be used in many recipees"""

    # might refactor later to work directly with an ID field if an actual database is to be used
    name: str = Field(description="The ingredient name and ID")
    standard_unit: StandardIngredientUnitsType = Field(
        description="The standard or most common unit of this ingredient"
    )

    def __hash__(self) -> int:
        """A hash function so the ingredient can be in a unique set"""
        return hash(self.name)
