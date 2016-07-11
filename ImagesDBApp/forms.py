from django import forms
from .models import Imagen

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
