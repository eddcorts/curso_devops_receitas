import pydantic


class BaseModel(pydantic.BaseModel):
    """Custom version of pydantic's BaseModel to activate orm_mode into the entities"""

    class Config:
        """Config class"""

        orm_mode = True
