from typing import Annotated, Any, List
from fastapi import APIRouter, Form, HTTPException, Path, Query
from sqlalchemy import Select
from models.category import categories
from models.post import posts
from databased import database
from schemas.category import Category
from schemas.post import Post
import uuid


router = APIRouter()

async def category_check(category_id : str):
    query = categories.select().where(categories.c.category_id == category_id)
    category = await database.fetch_one(query)
    return category
    
@router.post("/create/", response_model=Category)
async def create_category(name: str = Query(..., description='Введите название для создания категории')):
    category_id = str(uuid.uuid4())
    query = categories.insert().values(category_id=category_id,name=name)
    await database.execute(query)
    category = Category(category_id=category_id, name=name)
    return category

@router.get("/get/", response_model=List[Category])
async def get_categories():
    query = categories.select()
    return await database.fetch_all(query)

@router.get("/posts/{category_id}", response_model=List[Category])
async def get_posts_in_category(category_id: str = Path(..., description='Введите ID категории для вывода')):
    query = categories.select().where(categories.c.category_id == category_id)
    category = await database.fetch_one(query)
    if not await category_check(category_id):
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return category

@router.put("/update/{category_id}", response_model=Category)
async def update_category(category_id: str, name: str):
    query = categories.update().where(categories.c.category_id == category_id).values(name=name)
    await database.execute(query)
    category = Category(category_id=category_id, name=name)
    return category

@router.delete("/delete/{category_id}" , response_model=List[Category], description='При удалении категории удаляются посты которые относятся к этой категории')
async def delete_category(category_id: str = Path(..., description='Введите ID категории удаления')):
    query = categories.select().where(categories.c.category_id == category_id)
    category = await database.fetch_one(query)
    if not await category_check(category_id):
        raise HTTPException(status_code=404, detail="Категория не найдена")
    query = posts.delete().where(posts.c.category_id == category_id)
    await database.execute(query)
    query = categories.delete().where(categories.c.category_id == category_id)
    await database.execute(query)
    return {"message": "Категория и связанные с ней публикации успешно удалены"}    