# Шаблон проекта FastAPI

Это шаблон для проекта на FastAPI с миграциями Alembic и асинхронным подключением к базе данных PostgreSQL с использованием SQLAlchemy и Databases. Включает поддержку Docker и управление переменными окружения с помощью `python-dotenv`.

## Особенности

- FastAPI для создания API
- Асинхронная работа с базой данных через SQLAlchemy и Databases
- Alembic для управления миграциями базы данных
- Поддержка Docker для удобного развертывания
- Конфигурация переменных окружения через `python-dotenv`
- Логирование с использованием `colorlog`
- Полная настройка для разработки и продакшн-окружений

## Требования

- Python 3.9+
- PostgreSQL
- Docker (опционально, но рекомендуется)

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/MorisFromRTU/fastapi_project_template.git
   cd fastapi_project_template

## Запуск в Docker

1. Убедитесь, что Docker и Docker Compose установлены на вашем компьютере.

2. Создайте файл `.env` в корне проекта со следующим содержимым:

   ```env
   DATABASE_URL=postgresql+asyncpg://user:password@db/dbname

   Замените user, password и dbname на свои данные для подключения к базе данных.

3. Соберите и запустите контейнеры:
    
    docker-compose up --build

4. Чтобы выполнить миграции Alembic в Docker, используйте следующую команду:

    docker-compose run --rm web alembic upgrade head

## Структура проекта

.
├── app
│   ├── __init__.py
│   ├── main.py         # Точка входа для FastAPI приложения
│   ├── db.py           # Подключение к базе данных и управление сессиями
│   ├── models          # Модели SQLAlchemy
│   ├── schemas         # Схемы Pydantic
│   ├── crud.py         # CRUD операции
│   ├── routers
│   │   └── hello.py   # Маршруты API
│   └── alembic
│       └── versions    # Миграции Alembic
├── .env                # Переменные окружения
├── alembic.ini         # Конфигурация Alembic
├── Dockerfile          # Конфигурация Docker
├── docker-compose.yml  # Конфигурация Docker Compose
└── README.md           # Этот файл
