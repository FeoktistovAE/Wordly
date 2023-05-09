install:
	poetry install
lint:
	poetry run flake8 wordly/users
run:
	python3 manage.py runserver
migrations:
	python3 manage.py makemigrations
migrate:
	python3 manage.py migrate
console:
	python3 manage.py shell
test-coverage:
	poetry run pytest --cov=task_manager --cov-report xml
test:
	poetry run python3 manage.py test
messages:
	django-admin makemessages -l ru
compile:
	django-admin compilemessages