export PYTHONPATH=$(shell pwd)

all: deps tests doc

pypi:
	python setup.py sdist upload

clean:
	make -C docs clean
	-rm .coverage

run_examples:
	cd examples/graphviz; ./all.py
	cd examples/gephi; ./all.py

deps:
	pip install -r requirements/development.txt
	pip install -r requirements/documentation.txt

tests:
	py.test \
		--pep8 \
		--ignore=pycallgraph2/memory_profiler.py \
		test pycallgraph2 examples

	coverage run --source pycallgraph2,scripts -m py.test
	coverage report -m

	flake8 --exclude=__init__.py,memory_profiler.py pycallgraph2
	flake8 --ignore=F403 test
	flake8 examples

doc:
	cd docs/examples && ./generate.py
	cd docs/guide/filtering && ./generate.py

	make -C docs html man
	cp docs/_build/man/pycallgraph2.1 man/
	docs/update_readme.py

2to3:
	for a in pycallgraph2 test examples scripts; do 2to3 -wn $$a; done

