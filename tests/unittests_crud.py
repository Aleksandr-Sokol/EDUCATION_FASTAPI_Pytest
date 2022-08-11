import json
from starlette.testclient import TestClient
from app import app
from crud.data_crud import UserDataCRUD
from database.models import DbUser
# from conftest import override_get_db
from fastapi.encoders import jsonable_encoder


def test_get_data(test_db_session, datafix_read):
    print(test_db_session)
    data_crud = UserDataCRUD()
    # Для синхронного запуска
    d = json.loads(datafix_read('valid_person.json'))
    data_crud.create(test_db_session, **d)
    data_crud.create(test_db_session, **d)
    data_1 = data_crud.get(test_db_session, 1)
    data_2 = data_crud.get(test_db_session, 2)
    data_3 = data_crud.get(test_db_session, 3)
    assert data_1 is not None
    assert data_2 is not None
    assert jsonable_encoder(data_1) != jsonable_encoder(data_2)
    assert data_3 is None
