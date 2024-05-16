from typing import List
import uuid
import bcrypt
from fastapi import APIRouter, HTTPException
from app.models.user import users
from app.database import database
from app.schemas.user import User , UserResponse

router = APIRouter()

@router.post("/register/", response_model=UserResponse)
async def register_user(username: str, email: str, password: str):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    query = users.insert().values(
        username=username,
        email=email,
        hashed_password=hashed_password
    )
    last_record_id = await database.execute(query)
    return {**User(id=last_record_id, username=username, email=email, hashed_password=hashed_password).dict()}

@router.get("/get-users/", response_model=List[User])
async def get_users():
    query = users.select()
    return await database.fetch_all(query)

@router.delete("/delete-user/{user_id}", response_model=User)
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {"message": "Пользователь успешно удален"}
