"""Простое веб-приложение lab-app на Flask."""
import os
import socket

from flask import Flask

app = Flask(__name__)

# Строка подключения к PostgreSQL (если её нет - работаем без базы)
DATABASE_URL = os.getenv("DATABASE_URL")


def count_visit():
    """Записывает посещение и возвращает число посещений."""
    import psycopg2

    conn = psycopg2.connect(DATABASE_URL, connect_timeout=5)
    try:
        with conn, conn.cursor() as cur:
            cur.execute(
                "CREATE TABLE IF NOT EXISTS visits ("
                "id SERIAL PRIMARY KEY, "
                "visited_at TIMESTAMP DEFAULT now())"
            )
            cur.execute("INSERT INTO visits DEFAULT VALUES")
            cur.execute("SELECT count(*) FROM visits")
            return cur.fetchone()[0]
    finally:
        conn.close()


@app.route("/")
def index():
    # Главная страница: приветствие и имя хоста
    host = socket.gethostname()  # в контейнере это имя копии
    html = f"<h1>Hello from lab-app!</h1><p>Host: {host}</p>"
    if DATABASE_URL:
        try:
            visits = count_visit()
            html += f"<p>Visits stored in PostgreSQL: {visits}</p>"
        except Exception as exc:  # база недоступна
            html += f"<p>Database error: {exc}</p>"
    return html


@app.route("/health")
def health():
    # Проверка работоспособности: ответ в формате JSON
    return {"status": "ok"}


if __name__ == "__main__":
    # 0.0.0.0 - слушать все адреса, иначе контейнер недоступен извне
    app.run(host="0.0.0.0", port=5000)
