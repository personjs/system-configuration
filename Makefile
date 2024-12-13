all: clean install exe

build:
	poetry build
install:
	poetry install
exe:
	poetry run pyinstaller --name system-configuration --onefile src/system_configuration/main.py
clean:
	-find . -type d -name "__pycache__" -exec rm -rf {} +
	-find . -type f -name "*.pyc" -exec rm -f {} +
	-rm -rf dist/ build/ src/*.egg-info/ *.log
	-poetry cache clear pypi --all
run:
	poetry run python src/system_configuration/main.py

