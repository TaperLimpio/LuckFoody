from django.shortcuts import render
from  PaginaWeb.models import Usuario  # Asegúrate de que esta sea tu clase de usuario
from . import forms
from .forms import UsuarioForm,UsuarioAdminForm

# Create your views here.
def portalpago(request):
    return render(request,'portalpago.html')

def Repartidor(request):
    return render(request, "pagina-repartidor.html")


def ingresarplatillo(request):
    return render(request,"ingresarplatillo.html")

def verplatillo(request):
    return render(request, 'verplatillo.html')

def pagofracaso(request):
    return render(request,"pagofracaso.html")



def ingresarcatalogo(request):
    return render(request,"ingresar catalogo.html")

def paginaprincipal(request):
    return render(request,"paginaprincipal.html")

def ingresartrivia(request):
    return render(request,"ingresar trivia.html")

def Trivia(request):
    return render(request,"trivia.html")

def carritocompra(request):
    return render(request,'carrito.html')
