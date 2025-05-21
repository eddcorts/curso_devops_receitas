from pydantic import BaseModel

from ..data_source.recipee_data_source import RecipeeDataSource
from ..entity.recipee import Recipee, RecipeeID


class ReadRecipees(BaseModel):
    """Read one recipee"""

    recipee_data_source: RecipeeDataSource

    def execute(self, ids: set[RecipeeID] | None) -> list[Recipee]:
        """Run main class purpose"""
        return self.recipee_data_source.get_recipees(ids or set())
