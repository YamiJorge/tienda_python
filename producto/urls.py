"""tienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name='producto' #Agregamos un app_name para poder usar la propiedad de namespace
# de lo contrario arrojará un error.

urlpatterns = [
    #path('', views.hello_world, name = 'hello'),

    #Ahora reemplazaremos el "views.hello_world" por un ListView que mostrará lo mismo
    path('', views.ListaProducto.as_view(), name = 'hello'),

    #path('producto/<int:pk>', views.detalle_producto, name= "detalle_producto"),

    #Ahora reemplazaremos el "views.detalle_producto" por un ListView que mostrará lo mismo
    path('producto/<int:pk>', views.DetalleProducto.as_view(), name= "detalle_producto"),

    #En versiones de Django posteriores a la 1.9, para referenciar la PK en la URL
    # en este ejemplo es asi: path('producto/<int:pk>', views.detalle_producto, name= "detalle_producto")

    path('producto/nuevo', views.nuevo_producto, name= "nuevo_producto"),
    #Se declara una nueva URL que redirija al formulario donde ingresaremos los nuevos productos
]
