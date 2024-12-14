FROM python:3.9-slim

# Устанавливаем зависимости для работы
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл с зависимостями
COPY requirements.txt ./

# Устанавливаем зависимости
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Копируем всё приложение внутрь контейнера
COPY . .

# Указываем порт, который будет слушать приложение
EXPOSE 5000

# Задаём команду запуска Flask-приложения
CMD ["python", "app.py"]