![skills_workflow](https://github.com/D4rkLght/Skills/actions/workflows/Deploy.yml/badge.svg)
# Skills

Cервис Яндекс Практикума “Трекер развития”, позволяющего строить план обучения от точки А до точки Б.

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

1. Разработчик [Ярослав Андреев](https://github.com/D4rkLght)
2. Разработчик [Natalia Arlazarova](https://github.com/sic15)

# 2. Cсылка на веб хостинг <a id="host"></a>

- [Авторизация по yandex id](http://skills.sytes.net/accounts/yandex/login)
- [Сервис Skills](http://skills.sytes.net)
- [Swagger](http://skills.sytes.net/api/v1/swagger/)

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

Перед тем как запускать сервер локально, нужно подменить url на frontend части, чтобы отображались страницы.
Для этого нужно перейти по папкам hackathon/scr/utils/Api.js и в самом конце файла вставить url вместо имеющегося:
```shell
baseUrl: 'http://localhost/api/v1'
```

Запуск сервера локально:

запуск сервиса:
```shell
make server-init
```

остановка сервиса:
```shell
make stop
```

остановка контейнера сервиса:
```shell
make clear
```

# 4 Cтэк технологий <a id="stack"></a>

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)](https://gunicorn.org/)
[![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)](https://nginx.org/ru/)
[![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)](https://swagger.io/)
[![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/)
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)](https://www.django-rest-framework.org/)

# 5 Cторонние библиотеки <a id="library"></a>
[![Poetry](https://img.shields.io/badge/Poetry-464646?style=flat-square&logo=Poetry)](https://python-poetry.org/)
[![Ruff](https://img.shields.io/badge/Ruff-464646?style=flat-square&logo=Ruff)](https://docs.astral.sh/ruff/)
[![Pre-commit](https://img.shields.io/badge/Pre-commit-464646?style=flat-square&logo=Pre-commit)](https://pre-commit.com/)
[![Djoser](https://img.shields.io/badge/Djoser-464646?style=flat-square&logo&color=yellow)](https://github.com/sunscrapers/djoser)
[![SimpleJWT](https://img.shields.io/badge/SimpleJWT-464646?style=flat-square&logo&color=green)](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
[![Django-filter](https://img.shields.io/badge/Django-filter-464646?style=flat-square&logo&color=blue)](https://django-filter.readthedocs.io/en/stable/)