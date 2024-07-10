from sqlalchemy import Table, Column, Integer, String, ForeignKey, Text, DateTime , Boolean
from databased import metadata, engine

posts = Table(
    "posts",
    metadata,
    Column("post_id", String, primary_key=True),
    Column("title", String, nullable=False),
    Column("description", Text, nullable=False),
    Column("category_id", String, ForeignKey("categories.category_id")),
    Column("user_id", String, ForeignKey("users.user_id")),
    Column("published_at", DateTime, nullable=False),
    Column('is_published', Boolean , default=False),
)

metadata.create_all(engine)