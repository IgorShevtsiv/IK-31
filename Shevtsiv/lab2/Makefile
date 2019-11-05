.DEFAULT_GOAL := all

all: install test run deploy

install:
	@echo -e "Pipenv installation and virtual env..\n"
	@pip install pipenv
	@pipenv --python 3.7
	@pipenv install requests
	@pipenv install pytest
	
test:
	@echo -e "\n\nTesting..\n"
	@pipenv run pytest tests/tests.py | tee results.txt

run:
	@echo -e "\n\nRunning..\n"
	@pipenv run python app.py | tee -a results.txt

deploy:
	@echo -e "\n\nDeploying..\n"
	@git add results.txt
	@git commit -m "pushing results.txt"
	@git push origin master
