from django.shortcuts import render, redirect
from Sucursal_app.models import Sucursal
from . import forms
from .forms import SucursalForm

# Create your views here.

def listasucursal(request):
    sucursal = Sucursal.objects.all()
    data = {'sucursales':sucursal}
    return render(request, 'lista sucursales.html', data)

def ingresarsucursal(request):
    form=SucursalForm()
    if request.method == 'POST':
        form = SucursalForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("pagina-admin")
    data = {'form':form}
    return render(request,"ingresar sucursal.html", data)

def consultarsucursal(request,id):
    sucursal = Sucursal.objects.get(id=id)
    data={"sucursal":sucursal}
    return render(request, 'consultar sucursal.html',data)

def modificarsucursal(request,id):
    sucursal = Sucursal.objects.get(id=id)
    form = SucursalForm(instance=sucursal)
    if request.method == 'POST':
        form = SucursalForm(request.POST,instance=sucursal)
        if form.is_valid():
            form.save()
        return redirect("/pagina-admin/")
    data={'form':form}
    return render(request,'modificar sucursal.html',data)

def deshabilitarsucursal(request,id):
    sucursal = Sucursal.objects.get(id=id)
    sucursal.delete()
    return redirect("pagina-admin")