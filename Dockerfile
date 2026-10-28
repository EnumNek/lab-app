# Базовый образ: Python 3.12 в облегчённой версии
FROM python:3.12-slim

# Рабочая папка внутри контейнера
WORKDIR /app

# Сначала зависимости - этот слой кэшируется
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Затем код приложения
COPY app.py .

# Приложение слушает порт 5000
EXPOSE 5000
CMD ["python", "app.py"]
