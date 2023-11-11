start:
	poetry run flask --app flask_figlate/app --debug run --port 8000

start_unicorn:
	poetry run gunicorn flask_figlate.app:app

build:
	poetry lock;
	poetry install;