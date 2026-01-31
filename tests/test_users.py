from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_user():
    response = client.post(
        "/users",
        json={"name": "João", "email": "joao@email.com"}
    )

    assert response.status_code == 201
    data = response.json()

    assert data["name"] == "João"
    assert data["email"] == "joao@email.com"
    assert "id" in data


def test_get_users():
    response = client.get("/users")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_user_by_id():
    client.post(
        "/users",
        json={"name": "Maria", "email": "maria@email.com"}
    )

    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_update_user():
    client.post(
        "/users",
        json={"name": "Ana", "email": "ana@email.com"}
    )

    response = client.put(
        "/users/1",
        json={"name": "Ana Atualizada"}
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Ana Atualizada"


def test_delete_user():
    client.post(
        "/users",
        json={"name": "Pedro", "email": "pedro@email.com"}
    )

    response = client.delete("/users/1")
    assert response.status_code == 204


def test_get_user_not_found():
    response = client.get("/users/999")
    assert response.status_code == 404
