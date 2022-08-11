import json
import pytest
from httpx import AsyncClient
from app import app


# Синхронная
async def test_get_person(client):
    response = await client.get("/person/1")
    assert response.status_code == 200

# # Ассинхронная
# async def test_get_person_2(async_client: AsyncClient):
#     response = await async_client.get("/person/1")
#     assert response.status_code == 200

# @pytest.mark.asyncio, можно не использовать, Если указать asyncio_mode=auto
# # Ассинхронная
# async def test_get_person_1():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.get("/person/1")
#     assert response.status_code == 200


# Синхронная
def test_post_person(test_db_session, client, datafix_read):
    d = json.loads(datafix_read('valid_person.json'))
    response = client.post("/person/", json=d)
    assert response.status_code == 200
    assert response.json() != {}


# Ассинхронная
# async def test_post_person(async_client, datafix_read):
#     d = json.loads(datafix_read('valid_person.json'))
#     response = await async_client.post("/person/", json=d)
#     assert response.status_code == 200
#     assert response.json() != {}


# Ассинхронный клиент, в conftest.py
# @pytest.fixture
# async def async_client():
#     async with AsyncClient(app=app, base_url="http://test") as client:
#         yield client