build:
	echo "Build the site, output to 'output' directory"

test:
	pip install -e .
	cd tests && pytest -vv

build:
	pip install -e .
	sitegenerator build

serve:
	python -m http.server 8989 --directory public/
