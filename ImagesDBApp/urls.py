from django.conf import settings
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from ImagesDBApp.views import *



urlpatterns = [
    # Examples:
    url(r'^$', ListarImagenesIndex.as_view(), name='index'),
    url(r'^editImagenes/usuario=(?P<usuario>\w+)/$', ListarImagenesEdicion.as_view(),name='editImagenes'),
    url(r'^insertarImagen/(?P<username>\w+)/$', insertarImagen,name='insertarImagen'),
    url(r'^borrarImagen/(?P<pk>\d+)/$', borrarImagen,name='borrarImagen'),
    url(r'^editImagenes/$', ListarUsuariosEdicion.as_view(),name='editUsuarios'),
    url(r'^borrarUsuario/(?P<pk>\d+)/$', borrarUsuario,name='borrarUsuario'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
	urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
