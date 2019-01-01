from django.db import models
from cliente.models import Cliente
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=6, decimal_places=1)
    imagen = models.ImageField(blank=True)

    def __str__(self):
        return self.nombre

    class Meta: #Las Meta clases adentro de los modelos de Django sirven para adosar metadata a dichos modelos.
        ordering = ('id',)

class Favorito(models.Model):# Esta clase llamada Favorito es para enlazar
# Cliente y Producto con sus respectivas FK
    user = models.ForeignKey(Cliente, on_delete=models.CASCADE)#A partir de Django 2.x el Foreign key
# debe tener como parámetros la Clase a la cual se le va a obtener la FK y el "on_delete" en caso de que
# se borre el dato de la clase Favorito
    product = models.ForeignKey(Producto, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'

    def __str__(self): #Acá se retornan el nombre del cliente y del producto que se relacionan
#mediante sus respectivas FK
        return '%s %s' % (self.user.nombre , self.product.nombre)