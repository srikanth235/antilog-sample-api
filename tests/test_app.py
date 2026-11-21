import pytest

from app import create_app


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setenv("GREETING", "Hello")
    return create_app().test_client()


def test_health(client):
    assert client.get("/health").get_json() == {"ok": True}


def test_hello_defaults_to_world(client):
    assert client.get("/hello").get_json() == {"message": "Hello, world!"}


def test_hello_uses_the_name(client):
    assert client.get("/hello?name=Ada").get_json() == {"message": "Hello, Ada!"}


def test_app_refuses_to_start_without_a_greeting(monkeypatch):
    monkeypatch.delenv("GREETING", raising=False)
    with pytest.raises(RuntimeError):
        create_app()
