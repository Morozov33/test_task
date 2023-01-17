## Test task for trainer of YLab company.
### Status: [![linter](https://github.com/Morozov33/foods_menu_api/actions/workflows/linter.yml/badge.svg)](https://github.com/Morozov33/foods_menu_api/actions/workflows/linter.yml)  [![tests](https://github.com/Morozov33/foods_menu_api/actions/workflows/tests.yml/badge.svg)](https://github.com/Morozov33/foods_menu_api/actions/workflows/tests.yml)  [![Maintainability](https://api.codeclimate.com/v1/badges/a01595bc13c6dadfd0ad/maintainability)](https://codeclimate.com/github/Morozov33/foods_menu_api/maintainability)  [![Test Coverage](https://api.codeclimate.com/v1/badges/a01595bc13c6dadfd0ad/test_coverage)](https://codeclimate.com/github/Morozov33/foods_menu_api/test_coverage)
### It's usinig: ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)  ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)  ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
----
Для запуска на локальном сервере:
1. В файл `.env.example` добавить переменную `POSTGRES_DB_URL`.
2. Изменить имя файла `.env.example` на `.env`.
3. Запуск локального сервера с приложением командой `make start` из директории проекта. Устанавливаются все зависимости и к БД, указанной в переменной в `POSTGRES_DB_URL`, применяется последняя миграция из папки `foods_menu_api/migrations/versions`. После остановки приложения из базы данных удаляются все записи.
----
Скриншот успешных тестов к первому заданию:
![First test](https://github.com/Morozov33/foods_menu_api/blob/32cbc7212700602e4a10141b0a4daa5b890400c8/screnshoots/first_test_15-01-23.png)
