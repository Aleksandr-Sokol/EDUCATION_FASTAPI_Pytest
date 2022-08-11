import json


def test_get_person(client):
    response = client.get("/person/1")
    assert response.status_code == 200


def test_post_person(test_db_session, client, datafix_read):
    d = json.loads(datafix_read('valid_person.json'))
    response = client.post("/person/", json=d)
    print(response.json())
    assert response.status_code == 200
    assert response.json() != {}
