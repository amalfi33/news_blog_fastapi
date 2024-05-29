from typing import List
from pydantic import BaseModel, EmailStr
from .post import Post

class User(BaseModel):
    user_id: int
    username: str
    email: EmailStr
    hashed_password: str
    posts: List[Post] = []

    class Config:
        orm_mode = True
        
class UserResponse(BaseModel):
    username : str
    email : EmailStr
