

# Используйте минимальный образ Python
FROM python:3.10-slim

# Установите рабочую директорию внутри контейнера
WORKDIR /app

# Скопируйте файл requirements.txt и установите зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте оставшиеся файлы проекта
COPY . .

# Откройте порт 8000
EXPOSE 8000

# Запустите сервер Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
