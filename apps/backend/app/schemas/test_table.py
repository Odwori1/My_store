from pydantic import BaseModel
from pydantic import ConfigDict

class TableBase(BaseModel):
    name: str

class TableCreate(TableBase):
    pass

class Table(TableBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

    '''class Config:
        orm_mode = True'''
