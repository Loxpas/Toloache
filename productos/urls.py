from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ruta de la página principal, usando la vista 'index'
    path('productos/', views.lista_productos, name='lista_productos'),  # Ruta de lista de productos
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
]
