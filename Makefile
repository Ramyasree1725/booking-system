.PHONY: help install run test migrate seed docker-build docker-run

help:
	@echo "Available commands:"
	@echo "  make install      - Install Python dependencies"
	@echo "  make run          - Run the Django development server"
	@echo "  make test         - Run test suite with pytest"
	@echo "  make migrate      - Run database migrations"
	@echo "  make seed         - Seed demo data"
	@echo "  make docker-build - Build Docker container"
	@echo "  make docker-run   - Run application via Docker"

install:
	pip install -r requirements.txt

run:
	python manage.py runserver 0.0.0.0:8000

test:
	pytest

migrate:
	python manage.py migrate

seed:
	python manage.py seed_demo

docker-build:
	docker build -t booking-system .

docker-run:
	docker run -p 8000:8000 booking-system
