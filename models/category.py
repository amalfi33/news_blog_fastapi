from sqlalchemy import Table, Column, Integer, String, ForeignKey
from databased import metadata, engine

categories = Table(
    "categories",
    metadata,
    Column("category_id", String, primary_key=True),
    Column("name", String, nullable=False)
)

metadata.create_all(engine)
