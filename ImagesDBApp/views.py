from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import RegistroForm, ContactoForm
from .models import Registro


# Create your views here.
def base(request):
	return render(request, "base.html")

#Navbar
def sobre(request):
	return render(request, "sobre.html", {})

def home(request):
	titulo = 'Bienvenido'

	#Declaracion form
	form =  RegistroForm(request.POST or None)

	contexto = {
		"template_title": titulo,
		"a": 123,
		"form": form
	}

	if form.is_valid():
		instancia = form.save(commit=False)

		nombre = form.cleaned_data.get("nombre")
		if not nombre:
			nombre = "Nuevo nombre"
		instancia.nombre = nombre

		instancia.save()
		contexto = {
			"template_title": "Gracias"
		}

	if request.user.is_authenticated() and request.user.is_staff:
		queryset = Registro.objects.all().order_by('-fecha_registro')
		contexto = {
			"queryset": queryset
		}

	return render(request, "home.html",contexto)
