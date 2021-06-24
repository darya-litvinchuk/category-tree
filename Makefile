# Place your local stuff in Makefile.local
-include .env
-include Makefile.local

APP_NAME='web'
PROJECT_DIRECTORY='.'


.PHONY: build
build: 
	docker-compose build


.PHONY: build-nc
build-nc:
	docker-compose build --no-cache


.PHONY: up
up:
	docker-compose up --build
	

.PHONY: up-d	
up-d:
	docker-compose up --build -d


.PHONY: down	
down:
	docker-compose down


.PHONY: logs
logs:
	@#@ Show logs
	docker-compose logs -f ${APP_NAME}


.PHONY: shell-app
shell-app:
	docker-compose exec ${APP_NAME} /bin/bash


.PHONY: shell-db
shell-db:
	docker-compose exec db psql -U test_user test_db


.PHONY: create-superuser
create-superuser:
	docker-compose run ${APP_NAME} bash -c "python manage.py createsuperuser --noinput"


.PHONY: makemigrations
makemigrations:
	docker-compose run ${APP_NAME} bash -c "python manage.py makemigrations"


.PHONY: migrate
migrate:
	docker-compose run ${APP_NAME} bash -c "python manage.py migrate"


.PHONY: format
format:
	@#@ Run formatting using black and isort
	docker-compose run --rm ${APP_NAME} sh -c "black ${PROJECT_DIRECTORY} && isort ${PROJECT_DIRECTORY} "


.PHONY: lint
lint:
	@#@ Run all linters linter
	make format-check
	make flake8
	make mypy-check


.PHONY: format-check
format-check:
	@#@ Run formatting using black and isort
	docker-compose run --rm ${APP_NAME} sh -c "black ${PROJECT_DIRECTORY} --check && isort ${PROJECT_DIRECTORY} --check"


.PHONY: flake8
flake8:
	@#@ Run flake8
	docker-compose run --rm ${APP_NAME} flake8 ${PROJECT_DIRECTORY}


.PHONY: mypy
mypy:
	@#@ Run typechecking using mypy
	docker-compose run --rm ${APP_NAME} mypy ${PROJECT_DIRECTORY}


.PHONY: mypy-check
licenses-check:
	@#@ Run typechecking using mypy
	docker-compose run --rm ${APP_NAME} pip-licenses --summary
	docker-compose run --rm ${APP_NAME} pip-licenses --from=classifier --order=license


.PHONY: tests
tests:
	@#@ Run tests
	docker-compose -p test-category build
	docker-compose -p test-category run --rm web pytest --no-cov -s || true
	docker-compose -p test-category down -v
	

.PHONY: update
update:
	docker-compose pull && docker-compose build --pull --no-cache


.PHONY: clean
clean:
	docker-compose down -v


.PHONY: clean-cache
clean-cache:
	@#@ Clean junk files
	find . -name \*.pyc -delete
	find . -name __pycache__ -exec rm -rf {} \;
	rm -rf *.egg-info


.PHONY: drop-db
drop-db:
	@#@ Drop database
	docker-compose down
	docker volume rm pgdata


.PHONY: radon-check
radon-check:
	@#@ Check project source code metrics
	radon mi ${PROJECT_DIRECTORY}
	radon cc ${PROJECT_DIRECTORY} -a
