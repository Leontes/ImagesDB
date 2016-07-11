#!/bin/bash

wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh

heroku login

heroku config:set DISABLE_COLLECTSTATIC=1
heroku create

git add .
git commit -m "Despliegue heroku"
git push heroku master

heroku ps:scale web=1
heroku open
