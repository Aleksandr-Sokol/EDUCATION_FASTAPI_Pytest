from core.db import Base
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, sql


class UserData(Base):
    __tablename__ = "user_data"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    family = Column(String)
    age = Column(Integer)
