import sys
sys.path = ['', '..'] + sys.path[1:]
from core import Base
from typing import Optional, AsyncIterable
import pytest
from fastapi import Depends
from starlette.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine as Database
from sqlalchemy.orm import Session
from sqlalchemy_utils import database_exists, create_database, drop_database
from app import app
from core.db import get_db


SQLALCHEMY_DATABASE_URI = "sqlite:///example_test.db"
_db_conn = engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False})

def get_test_db_conn() -> Database:
    assert _db_conn is not None
    return _db_conn


def get_test_db() -> AsyncIterable[Session]:
    session = Session(bind=_db_conn)
    try:
        yield session
    finally:
        session.close()


@pytest.fixture(scope="session", autouse=True)
def create_test_database():
    if database_exists(SQLALCHEMY_DATABASE_URI):
        drop_database(SQLALCHEMY_DATABASE_URI)
    create_database(SQLALCHEMY_DATABASE_URI)  # Create the test database.
    Base.metadata.create_all(_db_conn)  # Create the tables.
    app.dependency_overrides[get_db] = get_test_db  # Mock the Database Dependency
    yield  # Run the tests.
    drop_database(SQLALCHEMY_DATABASE_URI)  # Drop the test database.


@pytest.fixture
def test_db_session():
    session = Session(bind=_db_conn)
    yield session
    for tbl in reversed(Base.metadata.sorted_tables):
        _db_conn.execute(tbl.delete())
    session.close()


@pytest.fixture()
def client():
    with TestClient(app) as client:
        yield client

# Ассинхронный клиент, в conftest.py
# @pytest.fixture
# async def async_client():
#     async with AsyncClient(app=app, base_url="http://test") as client:
#         yield client