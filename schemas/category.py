from typing import List
from pydantic import BaseModel
from schemas.post import Post

class Category(BaseModel):
    category_id: str
    name: str
    post : List[Post] = []

    class Config:
        from_attributes = True

class CategoryResponse(Category):
    name : str
    post : List[Post] = []