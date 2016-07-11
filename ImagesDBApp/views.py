from django.conf import settings
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from .forms import ImagenForm
from .models import Imagen
from django.contrib.auth.models import User

# Create your views here.
class ListarImagenesIndex(ListView):
	model = Imagen
	template_name = "index.html"


# Create your views here.
class ListarImagenesEdicion(ListView):
	model = Imagen
	template_name = "editImagenes.html"

	def get_queryset(self):
		if self.kwargs['usuario'] != "admin":
			self.usuario = User.objects.get(username=self.kwargs['usuario'])
			return Imagen.objects.filter(usuario=self.usuario)
		else:
			return Imagen.objects.all()


def insertarImagen(request, username):
	user = User.objects.get(username=username)
	img = Imagen(usuario = user, nombreImg = request.GET['nombreImg'], url_img  = request.GET['urlImg'])
	img.save()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def borrarImagen(request, pk):
	imagen = Imagen.objects.get(id=pk)
	imagen.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class ListarUsuariosEdicion(ListView):
	model = User
	template_name = "editUsuarios.html"


def borrarUsuario(request, pk):
	user = User.objects.get(id=pk)
	user.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
