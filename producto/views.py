from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Producto

def hello_world(request):
    producto = Producto.objects.order_by('id')
    template = loader.get_template('index.html')
    context = {
        'producto': producto
    }
    return HttpResponse(template.render(context, request))