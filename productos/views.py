from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria, ImagenProducto

def index(request):
    return render(request, 'index.html')

def lista_productos(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos, 'categorias': categorias})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    imagenes = producto.imagenes.all()  # Obtener todas las imágenes adicionales
    return render(request, 'productos/detalle_producto.html', {'producto': producto, 'imagenes': imagenes})

def galeria(request):
    return render(request, "galerias.html")

def talleres(request):
    return render(request, "talleres.html")