create-env:
	@conda create -n python_misc python=3.8 pip

install-tox:
	@pip install tox==4.5.2

tox:
	@tox
