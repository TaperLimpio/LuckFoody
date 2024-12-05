from django.shortcuts import render, redirect
from Sucursal_app.models import Sucursal
from . import forms
from .forms import SucursalForm

# Create your views here.
#lista con todas las sucursales en la base de datos
def listasucursal(request):
    sucursal = Sucursal.objects.all()
    data = {'sucursales':sucursal}
    return render(request, 'lista sucursales.html', data)


#funcion para poder ingresar sucursales a la base de datos desde la pagina web "siempre las crea de base con estado activo"
def ingresarsucursal(request):
    form=SucursalForm()
    if request.method == 'POST':
        form = SucursalForm(request.POST,request.FILES)
        if form.is_valid():
            sucursal = form.save(commit=False)
            sucursal.estado = "activo"
            sucursal.save()
        return redirect('/lista_sucursales/')
    data = {'form':form}
    return render(request,"ingresar sucursal.html", data)

#pirmite ver mas en detalle una sucursal selecionada y la detecta por el id
def consultarsucursal(request,id):
    sucursal = Sucursal.objects.get(id=id)
    data={"sucursal":sucursal}
    return render(request, 'consultar sucursal.html',data)

#permite actualizar los datos de una sucursal lo detecta por id
def modificarsucursal(request,id):
    sucursal = Sucursal.objects.get(id=id)
    form = SucursalForm(instance=sucursal)
    if request.method == 'POST':
        form = SucursalForm(request.POST,request.FILES,instance=sucursal)
        if form.is_valid():
            form.save()
        return redirect('/lista_sucursales/')
    data={'form':form}
    return render(request,'modificar sucursal.html',data)

#cambia el estado de una sucursal de "activo" a "inactivo"
def deshabilitarsucursal(request,id):
    sucursal = Sucursal.objects.get(id=id)
    if sucursal:
        sucursal.estado = "inactivo"
        sucursal.save()
    return redirect('/lista_sucursales/')

def habilitarsucursal(request,id):
    sucursal = Sucursal.objects.get(id=id)
    if sucursal:
        sucursal.estado = "activo"
        sucursal.save()
    return redirect('/lista_sucursales/')