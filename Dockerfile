# Sistema operativo
FROM ubuntu:14.04

# Autor
MAINTAINER José Ángel Segura Muros <shaljas@correo.ugr.es>


#Actualizar sistema base y prepararlo para la instalación de la aplicación
RUN apt-get -y update
RUN apt-get -y install sudo

# Instalacion
RUN sudo apt-get install -y git
RUN sudo apt-get install -y make
RUN git clone https://github.com/Leontes/ImagesDB.git

#Instalar la aplicación
WORKDIR ImagesDB
RUN make install


EXPOSE 8000
CMD make run_docker
