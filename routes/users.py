from typing import List
import uuid
import bcrypt
from fastapi import APIRouter, HTTPException
from models.user import users
from databased import database
from schemas.user import User , UserResponse

router = APIRouter()

@router.post("/register/", response_model=UserResponse)
async def register_user(username: str, email: str, password: str):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    query = users.insert().values(
        username=username,
        email=email,
        hashed_password=hashed_password
    )
    user_id = str(uuid.uuid4()) 
    await database.execute(query)
    user = User(
        user_id=user_id,
        username=username,
        email=email,
        hashed_password=hashed_password
    )
    return user

@router.get("/get/", response_model=List[User])
async def get_users():
    query = users.select()
    return await database.fetch_all(query)

@router.delete("/delete/{user_id}", response_model=User)
async def delete_user(user_id: str):
    query = users.delete().where(users.c.user_id == user_id)
    await database.execute(query)
    return {"message": "Пользователь успешно удален"}
