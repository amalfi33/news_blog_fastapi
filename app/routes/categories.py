from typing import Annotated, List
from fastapi import APIRouter, Form, HTTPException
from app.models.category import categories
from app.models.post import posts
from app.database import database
from app.schemas.category import Category
from app.schemas.post import Post
import uuid


router = APIRouter()

@router.post("/create/", response_model=Category)
async def create_category(name: Annotated[str, Form(..., description='Название')]):
    query = categories.insert().values(name=name)
    last_record_id =  await database.execute(query)
    return {**Category(category_id=last_record_id, name=name).dict()}

@router.get("/get/", response_model=List[Category])
async def get_categories():
    query = categories.select()
    return await database.fetch_all(query)

@router.get("/post/{category_id}", response_model=List[Post])
async def get_posts_in_category(category_id: int):
    query = categories.select().where(categories.c.category_id == category_id)
    category = await database.fetch_one(query)
    if category:
        query = posts.select().where(posts.c.category_id == category_id)
        category_posts = await database.fetch_all(query)
        return category_posts
    else:
        raise HTTPException(status_code=404, detail="Категория не найдена")

@router.put("/update/{category_id}", response_model=Category)
async def update_category(category_id: int, name: str):
    query = categories.update().where(categories.c.category_id == category_id).values(name=name)
    await database.execute(query)
    return {**Category(category_id=category_id, name=name).dict()}

@router.delete("/delete/{category_id}")
async def delete_category(category_id: int):
    query = categories.select().where(categories.c.category_id == category_id)
    category = await database.fetch_one(query)
    if not category:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    query = posts.delete().where(posts.c.category_id == category_id)
    await database.execute(query)
    query = categories.delete().where(categories.c.category_id == category_id)
    await database.execute(query)
    
    return {"message": "Категория и связанные с ней публикации успешно удалены"}    