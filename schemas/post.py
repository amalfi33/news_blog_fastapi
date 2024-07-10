from datetime import datetime
from pydantic import BaseModel

class Post(BaseModel):
    post_id: str
    title: str
    description: str
    category_id: str
    user_id: str
    published_at: datetime
    is_published: bool = False

    class Config:
        orm_mode = True