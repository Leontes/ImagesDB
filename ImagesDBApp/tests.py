from django.test import TestCase

# Create your tests here.
from django import forms
from .models import Usuario, Imagen
from .forms import UsuarioForm, ImagenForm

class TestsUsuarios(TestCase):
	def test_Usuarios(self):
		user = Usuario(email = 'email', nombre = 'nombre',apellidos = 'apellidos')
		user.save()

		user = Usuario.objects.get(email = 'email')

		self.assertEqual(user.nombre,'nombre')
		print("Se ha creado usuario, Test = OK")

	def test_cambiar_nombre(self):
		user = Usuario(email = 'email', nombre = 'nombre',apellidos = 'apellidos')
		user.save()

		user.nombre='CambioNombre'
		user.save()

		user = Usuario.objects.get(email = 'email')

		self.assertEqual(user.nombre,'CambioNombre')
		print("Se ha realizado el cambio de nombre, Test = OK")


	def test_cambiar_email(self):
		user = Usuario(email = 'email', nombre = 'nombre',apellidos = 'apellidos')
		user.save()

		user.email='CambioEmail'
		user.save()

		user = Usuario.objects.get(nombre = 'nombre')

		self.assertEqual(user.email,'CambioEmail')
		print("Se ha realizado el cambio de email, Test = OK")


class TestsImagenes(TestCase):
	def test_Imagenes(self):
		user = Usuario(email = 'email', nombre = 'nombre', apellidos = 'apellidos')
		user.save()

		img = Imagen(usuario = user, nombreImg = "nombreImagen",url_img  = 'www.servidordeimagenes/imagen.jpeg')
		img.save()

		img = Imagen.objects.get(usuario = user)

		self.assertEqual(img.url_img, 'www.servidordeimagenes/imagen.jpeg')
		print("Se ha creado una imagen, Test = OK")


	def test_cambiar_url_imagen(self):
		user = Usuario(email = 'email', nombre = 'nombre', apellidos = 'apellidos')
		user.save()

		img = Imagen(usuario = user, nombreImg = "nombreImagen", url_img  = 'www.servidordeimagenes/imagen.jpeg')
		img.save()

		img.url_img = 'www.servidordeimagenes/imagen.png'
		img.save();

		img = Imagen.objects.get(usuario = user)

		self.assertEqual(img.url_img, 'www.servidordeimagenes/imagen.png')
		print("Se ha modificado la url de una imagen, Test = OK")

	def test_cambiar_usuario_imagen(self):
		user1 = Usuario(email = 'email1', nombre = 'nombre1', apellidos = 'apellidos1')
		user1.save()

		img = Imagen(usuario = user1, nombreImg = "nombreImagen", url_img  = 'www.servidordeimagenes/imagen.jpeg')
		img.save()

		user2 = Usuario(email = 'email2', nombre = 'nombre2', apellidos = 'apellidos2')
		user2.save()

		img.usuario = user2
		img.save()

		img = Imagen.objects.get(usuario = user2)

		self.assertEqual(img.usuario, user2)
		print("Se ha modificado el usuario de una imagen, Test = OK")
