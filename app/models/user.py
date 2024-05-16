from sqlalchemy import Table, Column, Integer, String
from app.database import metadata, engine

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, nullable=False, unique=True),
    Column("email", String, nullable=False, unique=True),
    Column("hashed_password", String, nullable=False)
)

metadata.create_all(engine)