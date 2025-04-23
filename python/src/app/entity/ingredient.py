from typing import Literal

from pydantic import Field

from .base import BaseModel

type STANDARD_UNITS_TYPE = Literal[
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

    name: str = Field(description="The name of the ingredient")
    unit: STANDARD_UNITS_TYPE = Field(
        description="The standard unit of this ingredient"
    )
