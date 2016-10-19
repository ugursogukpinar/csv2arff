all: dev

dev:
	pip install -r requirements-dev.txt

# auto correct indentation issues
fix:
	autopep8 scripts --recursive  --select=E101,E121 --in-place
