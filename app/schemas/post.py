from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Post(BaseModel):
    post_id: int
    title: str
    description: str
    category_id: int
    user_id: int
    published_at: datetime
    is_published: bool = False

    class Config:
        orm_mode = True