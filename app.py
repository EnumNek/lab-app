"""Простое веб-приложение lab-app на Flask."""
import socket

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    # Главная страница: приветствие и имя хоста (в контейнере это его ID)
    return f"<h1>Hello from lab-app!</h1><p>Host: {socket.gethostname()}</p>"


@app.route("/health")
def health():
    # Проверка работоспособности: ответ в формате JSON
    return {"status": "ok"}


if __name__ == "__main__":
    # 0.0.0.0 - слушать все адреса, чтобы приложение было доступно из контейнера
    app.run(host="0.0.0.0", port=5000)
