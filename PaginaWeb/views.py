from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def portalpago(request):
    return render(request,'portalpago.html')

def ingresarplatillo(request):
    return render(request,"ingresarplatillo.html")