from typing import List
from pydantic import BaseModel, EmailStr
from .post import Post

class User(BaseModel):
    user_id: str
    username: str
    email: EmailStr
    hashed_password: str

    class Config:
        from_attributes = True
        
class UserResponse(BaseModel):
    username : str
    email : EmailStr
