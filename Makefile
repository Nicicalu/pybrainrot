# The following part is not depricated. It is used to publish new versions to 
# PyPI

release: 
	-rm -r dist
	python3 setup.py sdist bdist_wheel
	twine upload dist/*


test-release: 
	-rm -r dist
	python3 setup.py sdist bdist_wheel
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
