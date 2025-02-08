from django.contrib import admin
from .models import Categoria, Producto, ImagenProducto

class ImagenProductoInline(admin.TabularInline):
    model = ImagenProducto
    extra = 2  # Número de campos para agregar imágenes adicionales

class ProductoAdmin(admin.ModelAdmin):
    inlines = [ImagenProductoInline]  # Agrega las imágenes adicionales en el panel de administración
    list_display = ('nombre', 'categoria', 'precio', 'material', 'dimensiones', 'color')  # Campos a mostrar en la lista de productos

admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)