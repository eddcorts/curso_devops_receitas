from pydantic import BaseModel

from ..data_source.recipee_data_source import RecipeeDataSource
from ..entity.recipee import Recipee, RecipeeID


class DeleteRecipees(BaseModel):
    """Delete one recipee"""

    recipee_data_source: RecipeeDataSource

    def execute(self, ids: set[RecipeeID]) -> set[RecipeeID]:
        """Run main class purpose"""
        return self.recipee_data_source.delete_recipees(ids)
