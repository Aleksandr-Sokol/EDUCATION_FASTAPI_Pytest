from core.db import Base
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, sql


class PersonData(Base):
    __tablename__ = "person_data"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    family = Column(String)
    age = Column(Integer)


class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
