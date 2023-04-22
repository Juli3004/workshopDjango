from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings

# Para cambiar titulos en modulo admin
admin.site.site_header = 'Módulo Administrativo del workshop Django'       # default: "Django Administration"
admin.site.index_title = 'Tablas'                 # default: "Site administration"
admin.site.site_title = 'Workshop Django' # default: "Django site admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('productos/', include('appProductos.urls')),
    path('usuario/', include('appUsuarios.urls')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)