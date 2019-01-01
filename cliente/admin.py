from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)#Esto es un "decorador", el cual es una funcion externa que en este caso
# registra un cliente dentro del admin
class AdminClient(admin.ModelAdmin):#Clase Admin para administrar los clientes y desplegar lo que queremos ver
    list_display = ('nombre', 'telefono', 'email', 'direccion',) #list_display muestra lo que se indica
    list_filter = ('nombre',)#list_filter muestra lo que se indica
