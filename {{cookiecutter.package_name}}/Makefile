#
#
#

# ================================================================================
# configuration
# ================================================================================

SERVER_PORT		:= 8000
LIVERELOAD_PORT	:= 8001

DOCKER			:= docker
DOCKER_REPO		:= gpc_auth
DOCKER_TAG		:= latest


# ================================================================================
# setup
# ================================================================================

setup:
	pipenv install --dev


# ================================================================================
# development
# ================================================================================

dev:
	make -j2 server livereload SERVER_PORT=$(SERVER_PORT) LIVERELOAD_PORT=$(LIVERELOAD_PORT)

server:
	pipenv run ./manage.py migrate
	LIVERELOAD_PORT=$(LIVERELOAD_PORT) pipenv run ./manage.py runserver $(SERVER_PORT)

livereload:
	LIVERELOAD_PORT=$(LIVERELOAD_PORT) pipenv run ./manage.py livereload


# ================================================================================
# lint & test
# ================================================================================

lint:
	flake8 gpc_auth

test:
	pytest tests --driver chrome

test-unit:
	pytest tests/unit

test-e2e-chrome:
	pytest --driver chrome tests/e2e

test-e2e-firefox:
	pytest --driver firefox tests/e2e


# ================================================================================
# packaging
# ================================================================================

sdist:
	./setup.py sdist

docker:
	$(DOCKER) build -t $(DOCKER_REPO):$(DOCKER_TAG) .
