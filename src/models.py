from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Date,
)

from src.config import Base
from sqlalchemy.sql import func


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    created = Column(DateTime(timezone=True), server_default=func.now())
    modified = Column(DateTime(timezone=True), onupdate=func.now())
    name = Column(String)
    email = Column(String)
    gender = Column(String)
    birth_data = Column(Date)
    telephone = Column(String)
