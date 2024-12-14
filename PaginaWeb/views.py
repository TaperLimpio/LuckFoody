from django.shortcuts import render
from django.db.models import Count,F
from django.db.models.functions import TruncMonth
from django.utils import timezone
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta



from Usuario_app.models import Usuario
from Sucursal_app.models import Sucursal
from Platillo_app.models import Platillo, PlatilloSucursal
from Pedido_app.models import Pedido, lista_de_pedidos
from Catalogo_app.models import Catalogo
from Carrito_app.models import Carrito
from Trivia_app.models import Trivia,Descuentos


def dashboard(request):
    usuarios = Usuario.objects.all()
    usuarios_totales = usuarios.count()
    usuarios_activos = usuarios.filter(estado = "activo").count()
    usuarios_inactivos = usuarios.filter(estado = "activo").count()
    repartidores = Usuario.objects.filter(tipo = "repartidor")


    usuarios_pedidos = usuarios.values_list("nombre").annotate(pedidos_hechos = Count("pedidos_realizados")).order_by('-pedidos_hechos')
    usuario_del_mes = usuarios_pedidos[0]
    repartidores_pedidos = repartidores.values_list("nombre").annotate(pedidos_hechos = Count("pedidos_tomados")).order_by('-pedidos_hechos')
    repartidor_del_mes = repartidores_pedidos[0]

    sucursales = Sucursal.objects.all()

    platillos_mas_populares = lista_de_pedidos.objects.values_list("id_platillo__nombre").annotate(can_vendidas = Count("cantidad")).order_by('-cantidad')[:5]
    platillo_mas_vendido = platillos_mas_populares[len(platillos_mas_populares)-1]
    anno = datetime.now().year
    mes = datetime.now().month
    fecha_mes_inicio = datetime(day=1,month=mes,year=anno)
    fecha_mes_limite = datetime(day=1,month=mes,year=anno) + relativedelta(months=+1)
    platillos_vendidos_mes = Pedido.objects.filter(fechainicio__range = [fecha_mes_inicio,
                                                fecha_mes_limite],estado = 'entregado').count()

    pedidos = Pedido.objects.all()
    fecha_anno_inicio = datetime(day=1,month=1,year=anno)
    fecha_anno_limite = fecha_anno_inicio + relativedelta(months=+11,day=+31)
    print(fecha_anno_inicio)
    print(fecha_anno_limite)
    pre_pedidos_por_mes = pedidos.filter(fechainicio__range = [
        fecha_anno_inicio,fecha_anno_limite]).annotate(
            mes=TruncMonth('fechainicio')).values('mes').annotate(cantidad = Count('id')).values(
                'mes','cantidad'
            )
    
    pedidos_por_mes = [0,0,0,0,0,
                       0,0,0,0,0,
                       0,0]
    for pedidos in pre_pedidos_por_mes:
        pedidos_por_mes[(pedidos['mes'].month)-1] = pedidos['cantidad']
    print(pedidos_por_mes)
    pedidos_hechos_mes = Pedido.objects.filter(fechainicio__range = [fecha_mes_inicio,
                                                fecha_mes_limite]).count()
    pedidos_activos_mes = Pedido.objects.filter(fechainicio__range = [fecha_mes_inicio,
                                                fecha_mes_limite],estado = "activo").count()
    pedidos_entregados_mes = Pedido.objects.filter(fechainicio__range = [fecha_mes_inicio,
                                                fecha_mes_limite],estado = "entregado").count()
    pedidos_inactivos_mes = Pedido.objects.filter(fechainicio__range = [fecha_mes_inicio,
                                                fecha_mes_limite],estado = "inactivo").count()

    """
    NO USAR
    pedidos_por_mes = [{'mes':1,'cantidad':0},
                       {'mes':2,'cantidad':0},
                       {'mes':3,'cantidad':0},
                       {'mes':4,'cantidad':0},
                       {'mes':5,'cantidad':0},
                       {'mes':6,'cantidad':0},
                       {'mes':7,'cantidad':0},
                       {'mes':8,'cantidad':0},
                       {'mes':9,'cantidad':0},
                       {'mes':10,'cantidad':0},
                       {'mes':11,'cantidad':0},
                       {'mes':12,'cantidad':0}]
    for mes in pedidos_por_mes:
        for pedidos in pre_pedidos_por_mes:
            if mes["mes"] == pedidos['mes'].month:
                temp = {'mes':pedidos['mes'].month,'cantidad':pedidos['cantidad']}
                pedidos_por_mes.append(temp)
    """

    catalogos = Catalogo.objects.all()
    carritos = Carrito.objects.all()
    trivias = Trivia.objects.all()

    data = {
        'usuarios_totales':usuarios_totales,
        'usuarios_activos':usuarios_activos,
        'usuarios_inactivos':usuarios_inactivos,
        'usuario_del_mes':usuario_del_mes,
        'repartidor_del_mes':repartidor_del_mes,

        'platillos_mas_populares':platillos_mas_populares,
        'platillo_mas_vendido':platillo_mas_vendido,
        'platillos_vendidos_mes':platillos_vendidos_mes,

        'pedidos_por_mes':pedidos_por_mes,
        'pedidos_hechos_mes':pedidos_hechos_mes,
        'pedidos_activos_mes':pedidos_activos_mes,
        'pedidos_entregados_mes':pedidos_entregados_mes,
        'pedidos_inactivos_mes':pedidos_inactivos_mes
    }

    return render(request,'dashboard.html',data)