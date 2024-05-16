from datetime import datetime
from typing import List
import uuid
from fastapi import APIRouter, HTTPException
from app.models.post import posts
from app.database import database
from app.schemas.post import Post

router = APIRouter()

@router.post("/post-create/", response_model=Post)
async def create_post(title: str, content: str, category_id: int, user_id: int):
    post_id = str(uuid.uuid4())
    published_at = datetime.now()
    query = posts.insert().values(
        title=title,
        content=content,
        published_at=published_at,
        category_id=category_id,
        user_id=user_id
    )
    last_record_id = await database.execute(query)
    return {**Post(id=last_record_id, title=title, content=content, published_at=published_at, category_id=category_id, user_id=user_id).dict()}

@router.get("/get-posts/", response_model=List[Post])
async def get_posts():
    query = posts.select()
    return await database.fetch_all(query)

@router.put('/post-update/{post_id}', response_model=Post)
async def update_post(post_id: int, title: str, content: str):
    query = posts.update().where(posts.c.id == post_id).values(title=title, content=content)
    await database.execute(query)
    query = posts.select().where(posts.c.id == post_id)
    return await database.fetch_one(query)

@router.delete("/post-delete/{post_id}")
async def delete_post(post_id: int):
    query = posts.delete().where(posts.c.id == post_id)
    await database.execute(query)
    return {"message": "Публикация удалена успешно"}