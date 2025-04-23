from typing import Literal

from pydantic import Field

from .base import BaseModel
from .ingredient import STANDARD_UNITS_TYPE, Ingredient

type TIME_UNIT_TYPE = Literal["segundo", "minuto", "hora", "dia"] | str


class RecipeeIngredient(Ingredient):
    """The instance of the ingredient of one recipee with general specifications"""

    specification: str = Field(
        description="A specification for the ingredient (e.g. fatness, ripeness, branding etc.)"
    )
    quantity: float = Field(
        description="The amount of this ingredient to be used for the recipee in the told unit"
    )
    override_unit: STANDARD_UNITS_TYPE | None = Field(
        description="The actual unit to be used for this recipee. Leave empty to use the standard unit of the ingredient."
    )


class Recipee(BaseModel):
    """A recipee to cook a dish"""

    name: str = Field(description="The recipee name")
    time: float | None = Field(
        description="The expected time to do the recipee in the respective unit"
    )
    time_unit: TIME_UNIT_TYPE | None = Field(description="The time unit")
    steps: str = Field(
        description="The step by step text explaining how to do the recipee with given ingredients"
    )
    ingredients: set[RecipeeIngredient] = Field(
        description="Set of ingredients used in this recipee"
    )
