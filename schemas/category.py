
from pydantic import BaseModel

class Category(BaseModel):
    category_id: str
    name: str

    class Config:
        from_attributes = True