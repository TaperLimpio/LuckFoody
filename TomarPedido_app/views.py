from django.shortcuts import render, redirect
from django.utils import timezone
from Pedido_app.models import Pedido
from Usuario_app.models import Usuario

#Creacion de Aceptar Pedido
def aceptar_pedido(request,id_pedido):
    id = request.session['usuario_id']
    pedido_tomado = Pedido.objects.get(id = id_pedido)
    pedido_tomado.repartidor = Usuario.objects.get(id = id)
    pedido_tomado.estado = 'tomado'
    pedido_tomado.save()
    return redirect('pagina-repartidor')
#Creacion de Entrega Pedido
def entregar_pedido(request,id_pedido):
    id = request.session['usuario_id']
    pedido_tomado = Pedido.objects.get(id = id_pedido)
    pedido_tomado.estado = 'entregado'
    pedido_tomado.fechaentrega = timezone.now()
    pedido_tomado.save()
    return redirect('pagina-repartidor')
