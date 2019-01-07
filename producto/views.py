from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def detalle_producto(request, pk): #Acá se recibe un request y una PK
    producto = get_object_or_404(Producto, pk=pk)
    template = loader.get_template('detalle_producto.html')#Este template
    #mostrará el detalle del producto.
    context = {
        'producto': producto
    }
    return HttpResponse(template.render(context, request))


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

class ListaProducto(ListView):# Se crea una clase de tipo ListView
# para mostrar el modelo que en este caso será el de Producto
    model = Producto

class DetalleProducto(DetailView):# Se crea una clase de tipo DetailView
# para mostrar el detalle del modelo que en este caso será el de Producto
    model = Producto

def auth_login(request):# Se crea una función login para iniciar sesión en este proyecto
    if request.method == 'POST': #Si la petición del método es igual a POST
        action = request.POST.get('action', None) #se creará un form tanto de login como de registro
        username = request.POST.get('username', None) #Acá se solicitará el username
        password = request.POST.get('password', None) #Acá se solicitará el password para el login

        if action == 'signup':# Si la funcion es de crear usuario,  se creará
            #con su respectivo nombre y pass
            user = User.objects.create_user(username=username,
                                            password=password)
            user.save()
        elif action == 'login':#Si la función es la de login
            #comparará usuario y password. Si es así, iniciará sesión
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    context = {}
    return render(request, 'login/login.html', context)

