from django.db import models

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
