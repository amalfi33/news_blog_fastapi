from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Post(BaseModel):
    id: int
    title: str
    content: str
    published_at: datetime
    category_id: int
    user_id: int

    class Config:
        orm_mode = True