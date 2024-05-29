from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Post(BaseModel):
    post_id: int
    title: str
    content: str
    published_at: datetime
    category_id: int
    user_id: int
    is_published: bool = False

    class Config:
        orm_mode = True