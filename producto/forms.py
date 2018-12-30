from django import forms
#Acá crearemos un formulario para los productos
from .models import Producto


class ProductForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'