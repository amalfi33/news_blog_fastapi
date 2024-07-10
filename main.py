from contextlib import asynccontextmanager
from fastapi import FastAPI
from databased import database
from routes import users, categories, posts
import uvicorn
import uuid

app = FastAPI(
    title="news_blog",
    version="0.0.1",
)

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(categories.router, prefix="/categories", tags=["categories"])
app.include_router(posts.router, prefix="/posts", tags=["posts"])

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)