.PHONY: up build down logs test
up:
	docker-compose up --build
down:
	docker-compose down
build:
	docker-compose build
logs:
	docker-compose logs -f
test:
	cd backend && pytest -q
