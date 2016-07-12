# ImagesDB

##Badges
Versión [![PythonVersion](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/)
Licencia [![Hex.pm](https://img.shields.io/hexpm/l/plug.svg?maxAge=2592000)](http://www.apache.org/licenses/#2.0)
Travis CI [![Build Status](https://travis-ci.org/Leontes/ImagesDB.svg?branch=master)](https://travis-ci.org/Leontes/ImagesDB)
Shippable [![Run Status](https://api.shippable.com/projects/577f57263be4f4faa56c2f6b/badge?branch=master)](https://app.shippable.com/projects/577f57263be4f4faa56c2f6b)
Snap-ci [![Build Status](https://snap-ci.com/Leontes/ImagesDB/branch/master/build_image)](https://snap-ci.com/Leontes/ImagesDB/branch/master)
## José Ángel Segura Muros

Proyecto para la asignatura de Cloud Computing del Máster en Ingeniería Informática

## Hito 1
## Descripción
Este proyecto consistira en la creación de una web que permita a los usuarios que suban imagenes a la misma.

La web tendra las siguientes funcionalidades:
- [x]  Registro: Un usuario se registra en la aplicación, a través de usuario y contraseña.
- [x]  Subida de imagenes: Una vez registrado y logeado el usuario podra subir imagenes.
- [x]  Visualización de imagenes: Todas las imagenes subidas podran verse en la portada de la web.
- [x]  Gestion de imagenes: Los usuarios podran gestionar sus imagenes, los administradores podran gestionar todas las imagenes de la web.
- [x]  Gestion de usuarios: Los administradores podran gestionar a los usuarios, borrando o modificando la información de estos.

## Infraestructura Virtual necesaria
- [x]  Servidor de Base de Datos para la gestión de usuarios.
- [x]  Servidor de Base de Datos para el contenido de la Web.
- [x]  Servidor Web.

## Trabajaremos con las siguientes tecnologias
- [x]  Framework Django.
- [x]  Bases de Datos Gestionada con MySqL


##Hito 2
## Automatización **Make**
Se ha realizado un archivo [make](https://github.com/Leontes/ImagesDB/blob/master/Makefile) para automatizar el proceso.

El código del Makefile es el siguiente:
```
    #José Ángel Segura Muros
    #Makefile


    install:
      sudo apt-get -y update
      sudo apt-get install -y libmysqlclient-dev
      sudo apt-get install -y python-dev
      sudo apt-get install -y libjpeg8-dev
      sudo apt-get install -y libtiff4-dev
      sudo apt-get install -y zlib1g-dev
      sudo apt-get install -y libfreetype6-dev
      sudo apt-get install -y liblcms1-dev
      sudo apt-get install -y libwebp-dev
      sudo apt-get install -y libpq-dev
      sudo apt-get install -y postgresql-server-dev-all
      sudo apt-get install -y python-pip
      pip install --upgrade pip
      pip install -r requirements.txt

    light_install:
      sudo pip install -r requirements.txt

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

    doc:
      pycco *.py
      pycco ImagesDB*/*.py
```

Las opciones que contiene el archivo son las siguientes:

- Instalación del sistema (make ó make install)
- Instalación ligera del sistema para Snap-ci (make light_install)
- Actualización del sistema (make update)
- Limpieza (make clean)
- Realización Tests (make run_tests)
- Ejecución del servidor Django(make run)
- Documentación (make doc)

## Test, Sistema de Pruebas.
He creado varios test para verificar el funcionamiento de la aplicación web.

Los tests se dividen en dos bloques: Los tests de registro de usuarios y los tests de imagenes
###Tests de Usuarios
- [x] test_Usuarios, éste test crea un usuario y lo guarda.
```
  def test_Usuarios(self):
    user = User(username='Usuario1', email='mail@email.com', password='1234')
    user.save()

    user = User.objects.get(username = 'Usuario1')

    self.assertEqual(user.username,'Usuario1')
    print("Se ha creado usuario, Test = OK")
```

- [x] test_cambiar_nombre, éste test cambia el nombre a un usuario existente.
```
  def test_cambiar_nombre(self):
    user = User(username='Usuario1', email='mail@email.com', password='1234')
    user.save()

    user.username='CambioNombre'
    user.save()

    user = User.objects.get(username = 'CambioNombre')

    self.assertEqual(user.username,'CambioNombre')
    print("Se ha realizado el cambio de nombre, Test = OK")
```

- [x] test_cambiar_nombre, éste test cambia el mail a un usuario existente.
```
    def test_cambiar_email(self):
      user = User(username='Usuario1', email='mail@email.com', password='1234')
      user.save()

      user.email='CambioEmail@email.com'
      user.save()

      user = User.objects.get(username = 'Usuario1')

      self.assertEqual(user.email,'CambioEmail@email.com')
      print("Se ha realizado el cambio de email, Test = OK")
```

###Tests de Imagenes
- [x] test_Imagenes, éste test crea una imagen y la guarda.
```
    def test_Imagenes(self):
      user = User(username='Usuario1', email='mail@email.com', password='1234')
      user.save()

      img = Imagen(usuario = user, nombreImg = "nombreImagen", url_img  = 'www.servidordeimagenes/imagen.jpeg')
      img.save()

      img = Imagen.objects.get(usuario = user)

      self.assertEqual(img.url_img, 'www.servidordeimagenes/imagen.jpeg')
      print("Se ha creado una imagen, Test = OK")
```

- [x] test_cambiar_url_imagen, éste test cambia la dirección web de una imagen.
```
    def test_cambiar_url_imagen(self):
      user = User(username='Usuario1', email='mail@email.com', password='1234')
      user.save()

      img = Imagen(usuario = user, nombreImg = "nombreImagen", url_img  = 'www.servidordeimagenes/imagen.jpeg')
      img.save()

      img.url_img = 'www.servidordeimagenes/imagen.png'
      img.save();

      img = Imagen.objects.get(usuario = user)

      self.assertEqual(img.url_img, 'www.servidordeimagenes/imagen.png')
      print("Se ha modificado la url de una imagen, Test = OK")
```

- [x] test_cambiar_nombre_imagen, éste test cambia el nombre de una imagen.
```
    def test_cambiar_nombre_imagen(self):
      user = User(username='Usuario1', email='mail@email.com', password='1234')
      user.save()

      img = Imagen(usuario = user, nombreImg = "nombreImagen", url_img  = 'www.servidordeimagenes/imagen.jpeg')
      img.save()

      img.nombreImg = 'CambioNombreImagen'
      img.save();

      img = Imagen.objects.get(usuario = user)

      self.assertEqual(img.nombreImg, 'CambioNombreImagen')
      print("Se ha modificado el nombre de una imagen, Test = OK")
```

- [x] test_cambiar_usuario_imagen, éste test cambia el autor de una imagen.
```
    def test_cambiar_usuario_imagen(self):
      user1 = User(username='Usuario1', email='mail1@email.com', password='1234')
      user1.save()

      img = Imagen(usuario = user1, nombreImg = "nombreImagen", url_img  = 'www.servidordeimagenes/imagen.jpeg')
      img.save()

      user2 = User(username='Usuario2', email='mail2@email.com', password='1234')
      user2.save()

      img.usuario = user2
      img.save()

      img = Imagen.objects.get(usuario = user2)

      self.assertEqual(img.usuario, user2)
      print("Se ha modificado el usuario de una imagen, Test = OK")
```

## Integración Continua
Se ha desplegado el sistema en 3 plataformas distintas de Integración contínua

- [x] [Travis](https://travis-ci.org/) permite testear el código del proyecto. Para llevar a cabo esto hay que adjuntar en el directorio raíz de nuestro proyecto el fichero [**.travis.yml**](https://github.com/Leontes/ImagesDB/blob/master/.travis.yml).

El contenido del fichero .travis.yml es el siguiente:
```
    language: python
    python:
     - "2.7"
    # command to install dependencies
    install:
     - sudo apt-get install make
     - make install
    # command to run tests
    script:
     - make run_tests

    branches:
      - only:
        - master
```

- [x] [Shippable](https://app.shippable.com/) permite testear el código del proyecto. Para llevar a cabo esto hay que adjuntar en el directorio raíz de nuestro proyecto el fichero [**shippable.yml**](https://github.com/Leontes/ImagesDB/blob/master/shippable.yml).

El contenido del fichero shippable.yml es el siguiente:
```
    language: python
    python:
     - "2.7"
    # command to install dependencies
    install:
     - sudo apt-get install make
     - make install
    # command to run tests
    script:
     - make run_tests

    branches:
      - only:
        - master
```

- [x] [Snap-ci](https://snap-ci.com/) permite testear el código del proyecto. Para llevar a cabo esto hay que crear en la web de forma interactiva un pipeline con las ordenes que debe llevar a cabo la plataforma.

Las ordenes de programadas en la plaforma son las siguientes:
```
    yum install postgresql-devel
    make light_install
    make run_tests
```

## Documentación, **Pycco**
Para generar la documentación del proyecto usaremos Pycco. La generación esta programada directamente en el Makefile como se ha mostrado previamente.


##Hito 3
## Despliegue **Heroku**

El despligue se ha realizado sobre la plataforma Heroku. La aplicación puede encontrarse ya completamente funcional en la siguiente [**dirección**](https://imagesdb-cc.herokuapp.com/).

###Despligue automático de la app
Se ha creado un script que crea la aplicación, la configura y puebla la base de datos del Dyno. El script puede encontrarse en [heroku_deploy.sh](https://github.com/Leontes/ImagesDB/blob/master/heroku_deploy.sh) y su contenido es el siguiente:

```
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

```

Ademas es necesario un pequeño archivo [Procfile](https://github.com/Leontes/ImagesDB/blob/master/Procfile) para indicar el tipo de aplicación y los comandos necesarios para lanzarla.

```
    web: gunicorn ImagesDBApp.wsgi --log-file -
```

Además entrando en la configuración del Dyno en Heroku podemos activar los despligues automaticos cuando se hace un push en el repositorio de la manera que se muestra a continuación.

![Git](https://github.com/Leontes/ImagesDB/blob/master/readme-docs/git.png)

#Cambios en settings.py
Settings.py es el archivo que configura todo el proyecto Django. Debido a que hsata el momento se habia estado trabajando en local la base de datos configurada era un fichero guardado en disco. Esto a la hora de desplegarlo en Heroku no servía puesto que en este la BD estaba definida como un add-on y hay que acceder a ella a traves de una url.

Para solucionar este problema se ha modificado el archivo settings.py para que detecte si se está trabajando en local o en heroku para autodefinir la BD que debe usar. Los cambios son los siguientes:

```
    import dj_database_url
    if in_heroku:
        DATABASES = {'default' : dj_database_url.config()}
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.ImagesDB'),
            }
        }import dj_database_url
    if in_heroku:
        DATABASES = {'default' : dj_database_url.config()}
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.ImagesDB'),
            }
        }
```
