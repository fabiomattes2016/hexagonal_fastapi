from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import deferred
from app.infrastructure.database import Base


class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(255), unique=True, index=True)
    password = deferred(Column(String(100)))
