from sqlalchemy import Table, Column, Integer, String, ForeignKey, Text, DateTime , Boolean
from app.database import metadata, engine

posts = Table(
    "posts",
    metadata,
    Column("post_id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("content", Text, nullable=False),
    Column("published_at", DateTime, nullable=False),
    Column("category_id", Integer, ForeignKey("categories.id")),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column('is_published', Boolean , default=False),

)

metadata.create_all(engine)