#José Ángel Segura Muros
#Makefile


install:
	sudo apt-get -y update
	sudo apt-get install -y libmysqlclient-dev
	sudo apt-get install -y python-dev
	sudo apt-get install -y python-setuptools
	sudo apt-get install -y build-essential
	sudo apt-get install -y libjpeg8-dev
	sudo apt-get install -y libtiff4-dev
	sudo apt-get install -y zlib1g-dev
	sudo apt-get install -y libfreetype6-dev
	sudo apt-get install -y liblcms1-dev
	sudo apt-get install -y libwebp-dev
	sudo apt-get install -y libpq-dev
	sudo apt-get install -y postgresql-server-dev-all
	sudo easy_install pip
	pip install --upgrade pip
	pip install -r requirements.txt
	python manage.py makemigrations ImagesDBApp
	python manage.py migrate

light_install:
	pip install --upgrade pip
	pip install -r requirements.txt
	python manage.py makemigrations ImagesDBApp
	python manage.py migrate


update:
	sudo apt-get -y update
	sudo apt-get -y upgrade
	sudo pip install --upgrade -r  requirements.txt

clean:
	rm -rf *~* && find . -name '*.pyc' -exec rm {} \;


run_tests:
	python manage.py test ImagesDBApp

run:
	python manage.py runserver

run_docker:
		python manage.py runserver 0.0.0.0:8000


doc:
	pycco *.py
	pycco ImagesDB*/*.py
