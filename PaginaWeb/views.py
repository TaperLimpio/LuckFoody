from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def portalpago(request):
    return render(request,'portalpago.html')

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

def ingresarsucursal(request):
    return render(request,"ingresar sucursal.html")

def ingresartrivia(request):
    return render(request,"ingresar trivia.html")

def Trivia(request):
    return render(request,"trivia.html")