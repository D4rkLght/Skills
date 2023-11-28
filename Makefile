.SILENT:

COLOR_RESET = \033[0m
COLOR_GREEN = \033[32m
COLOR_YELLOW = \033[33m
COLOR_WHITE = \033[00m

.DEFAULT_GOAL := help


.PHONY: help
help:  # Вызвать help
	@echo -e "$(COLOR_GREEN)Makefile help:"
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "$(COLOR_GREEN)-$$(echo $$l | cut -f 1 -d':'):$(COLOR_WHITE)$$(echo $$l | cut -f 2- -d'#')\n"; done


start: # Запуск контейнеров сервиса
	docker-compose -f infra/dev/docker-compose.local.yaml up -d; \
	if [ $$? -ne 0 ]; \
    then \
        docker compose -f infra/dev/docker-compose.local.yaml up -d; \
		docker compose version; \
    fi

stop: # Остановка контейнеров сервиса
	docker-compose -f infra/dev/docker-compose.local.yaml down; \
	if [ $$? -ne 0 ]; \
    then \
		docker compose -f infra/dev/docker-compose.local.yaml down; \
	fi
	@sleep(3);

clear: # Очистка контейнеров сервиса
	docker-compose -f infra/dev/docker-compose.local.yaml down --volumes; \
	if [ $$? -ne 0 ]; \
    then \
		docker compose -f infra/dev/docker-compose.local.yaml down --volumes; \
	fi

migrate: # Выполнение миграций Django
	docker exec backend-container-skills poetry run python manage.py migrate

createsuperuser: # Создать супер пользователя
	docker exec backend-container-skills poetry run python manage.py createsuperuser --noinput

collectstatic:
	docker exec backend-container-skills poetry run python manage.py collectstatic --no-input

fixtures:
	docker exec backend-container-skills poetry run python manage.py loaddata fixtures/data.json

server-init: # Базовая команда для запуска БД, миграций, сервиса.
	make clear start migrate collectstatic createsuperuser

server-no-docker: # Базовая команда для запуска сервиса без докера.
	poetry run python backend/manage.py runserver --settings core.settings_for_tests
