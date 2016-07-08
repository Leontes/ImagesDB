#José Ángel Segura Muros
#Makefile


install:
	apt-get -y update
	apt-get install -y libmysqlclient-dev
	apt-get install -y python-dev
	apt-get install -y libjpeg8-dev
	apt-get install -y libtiff4-dev
	apt-get install -y zlib1g-dev
	apt-get install -y libfreetype6-dev
	apt-get install -y liblcms1-dev
	apt-get install -y libwebp-dev
	apt-get install -y python-pip
	pip install -r requirements.txt

light_install:
	sudo pip install -r requirements.txt

update:
	apt-get -y update
	apt-get -y upgrade
	pip install --upgrade -r  requirements.txt

clean:
	rm -rf *~* && find . -name '*.pyc' -exec rm {} \;


run_tests:
	python manage.py test ImagesDBApp

run:
	python manage.py runserver

doc:
	pycco *.py
	pycco ImagesDB*/*.py
