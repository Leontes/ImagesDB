#!/bin/bash

#Nos bajamos el toolbelt
wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh

#Nos logeamos en nuestra cuenta de Heroku
heroku login

#Creamos la app, linkamos el repostorio de Git con ella y la configuramos
heroku create imagesdb-cc
heroku git:remote -a imagesdb-cc
heroku config:set DISABLE_COLLECTSTATIC=1

#Hacemos un push del repostorio
git add .
git commit -m "Despliegue heroku"
git push heroku master

#Preparamos la aplicación para su funcionamiento(asignamos workers, creamos tablas en la DB, etc..)
heroku ps:scale web=1
heroku run make light_install

#Lanzamos la aplicación
heroku open
