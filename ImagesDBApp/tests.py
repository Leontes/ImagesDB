from django.test import TestCase
from django import forms
from .models import Imagen
from .forms import ImagenForm
from django.contrib.auth.models import User

# Create your tests here.

class TestsUsuarios(TestCase):
	def test_Usuarios(self):
		user = User(username='Usuario1', email='mail@email.com', password='1234')
		user.save()

		user = User.objects.get(username = 'Usuario1')

		self.assertEqual(user.username,'Usuario1')
		print("Se ha creado usuario, Test = OK")

	def test_cambiar_nombre(self):
		user = User(username='Usuario1', email='mail@email.com', password='1234')
		user.save()

		user.username='CambioNombre'
		user.save()

		user = User.objects.get(username = 'CambioNombre')

		self.assertEqual(user.username,'CambioNombre')
		print("Se ha realizado el cambio de nombre, Test = OK")


	def test_cambiar_email(self):
		user = User(username='Usuario1', email='mail@email.com', password='1234')
		user.save()

		user.email='CambioEmail@email.com'
		user.save()

		user = User.objects.get(username = 'Usuario1')

		self.assertEqual(user.email,'CambioEmail@email.com')
		print("Se ha realizado el cambio de email, Test = OK")


class TestsImagenes(TestCase):
	def test_Imagenes(self):
		user = User(username='Usuario1', email='mail@email.com', password='1234')
		user.save()

		img = Imagen(usuario = user, nombreImg = "nombreImagen", url_img  = 'www.servidordeimagenes/imagen.jpeg')
		img.save()

		img = Imagen.objects.get(usuario = user)

		self.assertEqual(img.url_img, 'www.servidordeimagenes/imagen.jpeg')
		print("Se ha creado una imagen, Test = OK")


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
