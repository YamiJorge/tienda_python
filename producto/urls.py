from django.urls import path
from . import views


from django.contrib.auth import views as auth_views #Acá hacemos otro import de views, pero con un alias
# para que no se repita el anterior

app_name='producto' #Agregamos un app_name para poder usar la propiedad de namespace
# de lo contrario arrojará un error.

urlpatterns = [

    #Se agrega una URL para el login
    path('login/', views.auth_login, name = "authentication"),

    #Se agrega una URL para el logout. Para Django 2.1, debe usarse LogoutView.asview()
    #y en el html configurar la página en la que el logout nos redirija.
    path('logout', auth_views.LogoutView.as_view(), name='logout'),

    #Ahora crearemos un ListView que mostrará el listado de productos
    path('', views.ListaProducto.as_view(), name = 'hello'),


    #Ahora reemplazaremos el "views.detalle_producto" por un ListView que mostrará lo mismo
    path('producto/<int:pk>', views.DetalleProducto.as_view(), name= "detalle_producto"),

    #En versiones de Django posteriores a la 1.9, para referenciar la PK en la URL
    # en este ejemplo es asi: path('producto/<int:pk>', views.detalle_producto, name= "detalle_producto")

    #Se declara una nueva URL que redirija al formulario donde ingresaremos los nuevos productos
    path('producto/nuevo', views.nuevo_producto, name= "nuevo_producto"),



]
