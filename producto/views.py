from django.http import HttpResponse, HttpResponseRedirect
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

"""def nuevo_producto(request):
    template = loader.get_template('nuevo_producto.html')
    form = ProductForm()
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))"""

def nuevo_producto(request):
    if request.method == 'POST': #Si la petición del método es igual a POST
        form = ProductForm(request.POST, request.FILES) # entonces el form será el ProductForm solicitado
        # además se agrega un request.FILES para solicitar archivos a cargar
        if form.is_valid(): #Si el form es válido
            product = form.save(commit=False) # entonces se guardará el producto ingresado
            # agregando al form.save un parámetro commit=False
            product.save()
            return HttpResponseRedirect('/')# Una vez guardado redirige a la raíz
    else:
        form = ProductForm() # Sino, el form tomará el valor de ProductForm

    template = loader.get_template('nuevo_producto.html')
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))