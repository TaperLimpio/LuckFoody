from django import forms
from Pedido_app.models import Pedido

#Filtro de deciciones 
FILTRO_DECICIONES_1=(
    ('Todo','----'),
    ('activo','activo'),
    ('inactivo','inactivo'),
    ('tomado','tomado'),
    ('entregado','entregado')
)
#Creacion Filtro Pedido
class FiltroPedido(forms.Form):
    estado = forms.ChoiceField(choices=FILTRO_DECICIONES_1)

#Creacion de los Pedidos
class PedidoForm(forms.Form):
    n_tarjeta = forms.CharField(max_length=19)
    direccion = forms.CharField(max_length=40)
    