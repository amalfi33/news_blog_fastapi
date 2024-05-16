from fastapi import FastAPI
from app.database import database
from app.routes import users, categories, posts

app = FastAPI(
    title="news_blog",
    version="0.0.1",
)

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(categories.router, prefix="/categories", tags=["categories"])
app.include_router(posts.router, prefix="/posts", tags=["posts"])

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()