from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Pedido, lista_de_pedidos
from .forms import FiltroPedido
from Usuario_app.models import Usuario


# Create your views here.
def consultar_pedidos(request):
    filtro = FiltroPedido()
    if request.method == "POST":
        filtro = FiltroPedido(request.POST)
        if filtro.is_valid():
            estado = filtro.cleaned_data['estado']
            if (estado == 'Todo'):
                pedidos = Pedido.objects.all()
            else:
                pedidos = Pedido.objects.filter(estado = estado)
    else:
        pedidos = Pedido.objects.all()
    data = {'pedidos':pedidos,'form':filtro}
    return render(request,'pedidos.html',data)

def ver_pedido(request,pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    lista_productos = lista_de_pedidos.objects.filter(id_pedido = pedido.id)
    return render(request, 'ver_pedido.html', {'pedido':pedido,'lista_productos':lista_productos})

def mis_pedidos(request):
    usuario_id = request.session['usuario_id']
    pedidos_activos = Pedido.objects.filter(
        Q(usuario = Usuario.objects.get(id=usuario_id)) & (Q(estado = 'activo') | Q(estado = 'tomado')))
    print(pedidos_activos)
        # estado = "activo",usuario = Usuario.objects.get(id=usuario_id)
    pedidos_pasados = Pedido.objects.filter(
        Q(usuario = Usuario.objects.get(id=usuario_id)) & Q(estado = "inactivo") | Q(estado = 'entregado'))
    return render(request,'mis_pedidos.html',{'ped_activos':pedidos_activos,
                                              'ped_pasados':pedidos_pasados})

def cancelar_pedido(request,id_pedido):
    pedido_tomado = Pedido.objects.get(id = id_pedido)
    pedido_tomado.estado = 'inactivo'
    pedido_tomado.save()
    return redirect('mis_pedidos')