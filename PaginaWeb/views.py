from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def portalpago(request):
    return render(request,'portalpago.html')

def Login(request):
    return render(request, "login.html")

def CrearCuenta(request):
    return render(request, "crear-cuenta.html")

def Administrador(request):
    return render(request, "pagina-admin.html")

def Repartidor(request):
    return render(request, "pagina-repartidor.html")

def CrearCuentaAdmin(request):
    return render(request, "crear-cuenta-admin.html")

def ingresarplatillo(request):
    return render(request,"ingresarplatillo.html")

def verplatillo(request):
    return render(request, 'verplatillo.html')

def pagofracaso(request):
    return render(request,"pagofracaso.html")

def pagoexitoso(request):
    return render(request,"pago exitoso.html")

def ingresarcatalogo(request):
    return render(request,"ingresar catalogo.html")

<<<<<<< HEAD
def ingresarsucursal(request):
    return render(request,"ingresar sucursal.html")

def ingresartrivia(request):
    return render(request,"ingresar trivia.html")

def Trivia(request):
    return render(request,"trivia.html")
=======
def carritocompra(request):
    return render(request,'carrito.html')
>>>>>>> d19271b79bda43467a4d1611afd430d94c2c8851
