"""Автотесты приложения lab-app (запускаются командой pytest)."""
from app import app


def test_index():
    # Тестовый клиент Flask отправляет запрос без запуска веб-сервера
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello from lab-app!" in response.data


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
