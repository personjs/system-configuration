all: clean build install

run:
	poetry run python ./src/system_configuration/main.py
build:
	poetry build
install:
	poetry install
dist:
	python setup.py clean sdist
clean:
	-find . -type d -name "__pycache__" -exec rm -rf {} +
	-find . -type f -name "*.pyc" -exec rm -f {} +
	-rm -rf dist/ build/ src/*.egg-info/
	-poetry cache clear pypi --all
	-poetry env remove python

