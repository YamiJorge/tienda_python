from django.contrib import admin
from .models import Producto, Favorito


#admin.site.register(Producto)
@admin.register(Producto)#Esto es un "decorador", el cual es una funcion externa que en este caso
# registra un producto dentro del admin
class AdminProducto(admin.ModelAdmin): #Clase Admin para administrar los productos y desplegar lo que queremos ver
    list_display = ('id', 'nombre', 'categoria', 'descripcion', 'precio',) #list_display muestra lo que se indica
    list_filter = ('categoria',)#list_filter filtra lo que se indica


@admin.register(Favorito)#Esto es un "decorador", el cual es una funcion externa que en este caso
# registra un producto favorito dentro del admin
class AdminFavorite(admin.ModelAdmin): #Clase Admin para administrar los productos y desplegar lo que queremos ver
    list_display = ('user', 'product',) #list_display muestra lo que se indica
    list_filter = ('user', 'product',)#list_filter filtra lo que se indica

