front-serv:
	cd ./Front-vuejs/; npm run serve

back-serv:
	cd ./Back-django/; ./manage.py runserver

install:
	pip install -r ./Back-django/requirements.txt
	npm install ./Front-vuejs