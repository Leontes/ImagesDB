from django.conf import settings
from django.views.generic import ListView
from .forms import UsuarioForm, ImagenForm
from .models import Usuario, Imagen


# Create your views here.
class ListarImagenes(ListView):
	model = Imagen
	template_name = "index.html"
