#José Ángel Segura Muros
#Makefile

install:
	sudo apt-get update
	sudo apt-get upgrade
	sudo apt-get install -y libmysqlclient-dev
	sudo apt-get install -y python-dev
	sudo apt-get install -y libjpeg8-dev
	sudo apt-get install -y libtiff4-dev
	sudo apt-get install -y zlib1g-dev
	sudo apt-get install -y libfreetype6-dev
	sudo apt-get install -y liblcms1-dev
	sudo apt-get install -y libwebp-dev
	sudo apt-get install -y python-pip
	sudo pip install -r requirements.txt

light_Install:
	sudo pip install -r requirements.txt

clean:
	rm -rf *~* && find . -name '*.pyc' -exec rm {} \;


run_tests:
	python manage.py test ImagesDBApp

run:
	python manage.py runserver

doc:
	pycco *.py
	pycco ImagesDB*/*.py
