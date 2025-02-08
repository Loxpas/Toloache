from django.contrib import admin  
from django.urls import path, include  
from django.conf import settings
from django.conf.urls.static import static
from productos.views import index, galeria, talleres  # Importa ambas vistas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('productos.urls')),  # Usa productos.urls para manejar la página principal y productos
    path("galeria/", galeria, name="galeria"),  # Corrige la vista a galeria sin 'views.'
    path("talleres/", talleres, name="talleres"), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
