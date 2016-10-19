all: test

dev:
	pip install -r requirements-dev.txt

# auto correct indentation issues
fix:
	autopep8 scripts --recursive --in-place

test:
	pytest --pep8 --cov
