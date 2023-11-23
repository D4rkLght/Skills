# Skills

# Содержание

1. [Cведения о команде](#info)
2. [Cсылка на веб хостинг](#host)
3. [Подготовка к запуску](#start)

    3.1. [Правила работы с git](#git)

    3.2. [Настройка переменных окружения](#env)

    3.3. [Запуск сервера локально](#local)

4. [Cтэк технологий](#stack)
5. [Cсылки на сторонние библиотеки](#library)


# 1. Cведения о команде: <a id="info"></a>

1. Разработчик [Ярослав Андреев ](https://github.com/D4rkLght)

# 2. Cсылка на веб хостинг <a id="host"></a>


# 3. Подготовка к запуску <a id="start"></a>

Примечание: использование Docker, poetry.

## 3.1. Правила работы с git (как делать коммиты и pull request-ы)<a id="git"></a>:

1. Две основные ветки: `main` и `develop`
2. Ветка `develop` — “предрелизная”. Т.е. здесь должен быть рабочий и выверенный код
3. Создавая новую ветку, наследуйтесь от ветки `develop`
4. В `main` находится только production-ready код (CI/CD)
5. Правила именования веток
   - весь новый функционал — `feature/название-функционала`
   - исправление ошибок — `bugfix/название-багфикса`
6. Пушим свою ветку в репозиторий и открываем Pull Request


## 3.2. Настройка переменных окружения <a id="env"></a>

Перед запуском проекта необходимо создать копию файла
```.env.example```, назвав его ```.env``` и установить значение базы данных почты и тд.

### Системные требования
- Python 3.11+;
- Docker (19.03.0+) c docker compose;
- [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer);

Установка зависимостей poetry:

```shell
poetry install
```

## 3.3. Запуск сервера локально <a id="local"></a>

Запуск сервера локально:

запуск сервиса:
```shell
make start
```

остановка сервиса:
```shell
make stop
```

остановка контейнера сервиса:
```shell
make clear
```

Базовая команда для запуска БД, миграций, сервиса:
```shell
docker exec backend-container-skills make server-init
```

наполнение PostgreSQL тестовыми данными:
```shell
docker exec backend-container-skills poetry run python manage.py loaddata fixtures/data.json
```

# 4 Cтэк технологий <a id="stack"></a>

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)](https://gunicorn.org/)
[![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)](https://nginx.org/ru/)
[![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)](https://swagger.io/)
[![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/)
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

# 5 Cторонние библиотеки <a id="library"></a>

