from sqlalchemy import Table, Column, Integer, String, ForeignKey, Text, DateTime
from app.database import metadata, engine

posts = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("content", Text, nullable=False),
    Column("published_at", DateTime, nullable=False),
    Column("category_id", Integer, ForeignKey("categories.id")),
    Column("user_id", Integer, ForeignKey("users.id")),

)

metadata.create_all(engine)