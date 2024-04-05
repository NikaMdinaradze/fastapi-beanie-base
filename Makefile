build:
	@echo "building API test server docker"
	docker-compose build

run:
	@echo "starting API test server docker"
	docker-compose up

run_detached:
	@echo "starting API test server docker"
	docker-compose up -d

run_tests:
	@echo "running tests docker"
	docker-compose run --rm api sh -c "pytest"
