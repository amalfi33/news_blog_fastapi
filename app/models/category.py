from sqlalchemy import Table, Column, Integer, String, ForeignKey
from app.database import metadata, engine

categories = Table(
    "categories",
    metadata,
    Column("category_id", Integer, primary_key=True),
    Column("name", String, nullable=False)
)

metadata.create_all(engine)
