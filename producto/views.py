from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Producto
from .forms import ProductForm

def hello_world(request):
    producto = Producto.objects.order_by('id')
    template = loader.get_template('index.html')
    context = {
        'producto': producto
    }
    return HttpResponse(template.render(context, request))

def detalle_producto(request, pk): #Acá se recibe un request y una PK
    producto = get_object_or_404(Producto, pk=pk)
    template = loader.get_template('detalle_producto.html')#Este template
    #mostrará el detalle del producto.
    context = {
        'producto': producto
    }
    return HttpResponse(template.render(context, request))

def nuevo_producto(request):
    template = loader.get_template('nuevo_producto.html')
    form = ProductForm()
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))