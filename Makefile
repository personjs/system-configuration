all: run

run:
	python src/system_configuration/main.py
install:
	pip install -e .
dist:
	python setup.py clean sdist
dist-install:
	pip install dist/*.tar.gz
clean:
	python setup.py clean