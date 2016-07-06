from django.contrib import admin

# Register your models here.
from .forms import UsuarioForm
from .models import Usuario, Imagen

class UsuarioAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "fecha_registro", "actualizado"]
	#class Meta:
	#	model = Registro
	form = UsuarioForm

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Imagen)
