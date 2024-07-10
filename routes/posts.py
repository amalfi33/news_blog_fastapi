from datetime import datetime
from typing import List
import uuid
from fastapi import APIRouter, HTTPException, Path, Query
from models.post import posts
from databased import database
from schemas.post import Post

router = APIRouter()

@router.post("/create/", response_model=Post)
async def create_post(title: str = Query(),
                    description: str= Query(),
                    category_id: str = Query(..., description='Введите ID категории'),
                    user_id: str = Query(..., description='Введите ID автора'),
                    is_published : bool = Query(False, description='Публикация поста')
                    ):
    published_at = datetime.now()
    query = posts.insert().values(title=title,description=description,published_at=published_at,category_id=category_id, user_id=user_id , is_published=is_published)
    post_id = str(uuid.uuid4())
    await database.execute(query)
    post = Post(
        post_id=post_id,
        title=title,
        description=description,
        published_at=published_at,
        category_id=category_id,
        user_id=user_id
        )
    return post

@router.get("/get/", response_model=List[Post])
async def get_posts():
    query = posts.select()
    return await database.fetch_all(query)


@router.get('/get-id/{post_id}', response_model=List[Post])
async def get_post_id(post_id: str = Path(..., description='Введите ID поста для вывода')):
    query = posts.select().where(posts.c.post_id == post_id)
    post = await database.fetch_one(query)
    if post is None:
        raise HTTPException(status_code=404, detail="Пост не был найден")       
    return post


@router.put('/update/{post_id}', response_model=Post)
async def update_post(post_id: str, title: str, content: str):
    query = posts.update().where(posts.c.post_id == post_id).values(title=title, content=content)
    await database.execute(query)
    query = posts.select().where(posts.c.post_id == post_id)
    return await database.fetch_one(query)

@router.delete("/delete/{post_id}", response_model=List[Post])
async def delete_post(post_id: str = Path(..., description='Введите ID поста для удаления')):
    query = posts.delete().where(posts.c.post_id == post_id)
    await database.execute(query)
    return {"message": "Публикация удалена успешно"}