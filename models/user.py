from sqlalchemy import Table, Column, Integer, String
from databased import metadata, engine

users = Table(
    "users",
    metadata,
    Column("user_id", String, primary_key=True),
    Column("username", String, nullable=False, unique=True),
    Column("email", String, nullable=False, unique=True),
    Column("hashed_password", String, nullable=False)
)

metadata.create_all(engine)