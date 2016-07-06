from django import forms
from .models import Usuario, Imagen

class UsuarioForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = ['email', 'nombre','apellidos']


	#Validaciones
	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')
		if not domain == "gmail":
			raise forms.ValidationError("Debe utilizar una cuenta de Gmail")
		if not extension == "com":
			raise forms.ValidationError("Por favor, la extension debe ser .com")
		return email

	def clean_nombre(self):
		nombre = self.cleaned_data.get('nombre')
		return nombre

	def clean_apellidos(self):
		apellidos = self.cleaned_data.get('apellidos')
		return apellidos


class ImagenForm(forms.ModelForm):
	class Meta:
		model = Imagen
		fields = ['usuario', 'url_img']

	#Validaciones
	def clean_usuario(self):
		user = self.cleaned_data.get('usuario')
		if not self.instance.usuario.filter(usuario=usuario).count():
			raise forms.ValidationError("El usuario no se encuentra")
		return user

	def clean_url(self):
		url = self.cleaned_data.get('url_img')
		return url
