install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
post-install:
	#post-install
format:
	#format code
	black *.py tradegptpub/*.py tradegptpub/*/*.py
lint:
	#pylint
	pylint --disable=R,C *.py tradegptpub/*.py
test:
	#test
	python -m pytest -vv --cov=tradegptpub --cov=main test_*.py
build:
	#build container
	# docker build -t deploy_tradegptpub .
run:
	#run docker
	# docker run -p 127.0.0.1:8080:8080 190a9ded6f6d
deploy:
	#deploy
all: install post-install lint test deploy