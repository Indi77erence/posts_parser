### Для запуска
Склонировать к себе на хост проект и заменить данные в .env на свои.
Выполнить в терминале:
1. pip install -r requirements.txt
2. alembic revision --autogenerate -m "create_db"
3. alembic upgrade head 
4.uvicorn src.main:create_app --reload

Сервис будет доступен по адресу http://127.0.0.1:8000/docs#

P.S. В докере не запстился, так как webdriver не смог сказачть для unix-системы драйвер при парсинге.
