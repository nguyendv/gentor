build:
	echo "Build the site, output to 'output' directory"

test:
	pip install -e .
	cd tests && pytest -vv