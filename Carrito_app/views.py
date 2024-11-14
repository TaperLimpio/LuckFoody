from django.shortcuts import render, redirect
from django.db.models import Sum
from django.utils import timezone
from .models import Carrito
from Usuario_app.models import Usuario
from Platillo_app.models import Platillo
from Pedido_app.models import Pedido, lista_de_pedidos
from Pedido_app.forms import PedidoForm


def agregar_a_carrito(request,platillo_id):
    id = request.session['usuario_id']
    try:
        carrito= Carrito.objects.get(id_platillo = platillo_id, id_usuario = id)
        carrito.cantidad += 1
        carrito.precio = carrito.id_platillo.precio * carrito.cantidad
        carrito.save()
    except Carrito.DoesNotExist:
        carrito = Carrito()
        carrito.id_usuario = Usuario.objects.get(id=id)
        carrito.id_platillo = Pedido.objects.get(id=platillo_id)
        carrito.cantidad = 1
        carrito.precio = carrito.id_platillo.precio * carrito.cantidad
        carrito.save()
    return redirect('mi_carrito', usuario_id = id)

def ver_carrito(request,usuario_id):
    carrito = Carrito.objects.filter(id_usuario = usuario_id)
    total = carrito.aggregate(Sum('precio'))
    return render(request, 'carrito.html',{'carrito':carrito,'total':total['precio__sum']})

def aumentar_cantidad(request,pedido_carrito_id):
    id = request.session['usuario_id']
    try:
        carrito = Carrito.objects.get(id = pedido_carrito_id)
        carrito.cantidad += 1
        carrito.precio = carrito.id_platillo.precio * carrito.cantidad
        carrito.save()
    except Carrito.DoesNotExist:
        print("no existe")
    return redirect('mi_carrito',usuario_id = id)

def disminuir_cantidad(request,pedido_carrito_id):
    id = request.session['usuario_id']
    try:
        carrito = Carrito.objects.get(id = pedido_carrito_id)
        if carrito.cantidad <= 1:
            carrito.delete()
        else:
            carrito.cantidad -= 1
            carrito.precio = carrito.id_platillo.precio * carrito.cantidad
            carrito.save()
    except Carrito.DoesNotExist:
        print("no existe")
    return redirect('mi_carrito',usuario_id = id)

def realizar_pedido(request):
    id = request.session['usuario_id']
    carrito = Carrito.objects.filter(id_usuario = id)
    form = PedidoForm()
    if request.method == "POST":
        print(request.POST)
        if form.is_valid:
            pedir(request,data = {'direccion':request.POST['direccion']})
            return redirect('pago exitoso')
    return render(request,'realizar_pedido.html',{'form':form})

def pedir(request,data):
    print("se esta generando el pedido")
    id = request.session['usuario_id']
    carrito = Carrito.objects.filter(id_usuario = id)
    pre_pedido = Pedido()
    pre_pedido.repartidor = Usuario.objects.get(id = 2)
    pre_pedido.usuario = Usuario.objects.get(id = id)
    pre_pedido.estado = "activo"
    pre_pedido.fechaentrega = timezone.now()
    pre_pedido.descuento = 0.0
    pre_pedido.direccion = data["direccion"]
    print(carrito.aggregate(Sum('precio')))
    pre_pedido.total = carrito.aggregate(Sum('precio'))['precio__sum']
    pre_pedido.save()
    for car in carrito:
        lista = lista_de_pedidos()
        lista.id_pedido = pre_pedido
        lista.id_platillo = car.id_platillo
        lista.cantidad = car.cantidad
        lista.save()
    print("Se termino y guardo el pedido")
    carrito.delete()

def pagoexitoso(request):
    id = request.session['usuario_id']
    pedido = Pedido.objects.get(usuario = id, estado = 'activo')
    return render(request,"pagoexitoso.html",{'pedido':pedido})

def pagofracaso(request):
    return render(request,"pagofracaso.html")