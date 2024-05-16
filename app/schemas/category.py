from typing import List
from pydantic import BaseModel
from .post import Post

class Category(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True