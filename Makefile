all: test

dev:
	pip install -r requirements.txt -r requirements-dev.txt

# auto correct indentation issues
fix:
	autopep8 csv2arff --recursive --in-place
	autopep8 tests --recursive --in-place

test:
	pytest --pep8 --cov -s
