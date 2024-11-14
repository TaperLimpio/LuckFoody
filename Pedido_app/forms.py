from django import forms
from Pedido_app.models import Pedido

FILTRO_DECICIONES_1=(
    ('Todo','----'),
    ('activo','activo'),
    ('inactivo','inactivo'),
    ('tomado','tomado'),
    ('entregado','entregado')
)

class FiltroPedido(forms.Form):
    estado = forms.ChoiceField(choices=FILTRO_DECICIONES_1)

class PedidoForm(forms.Form):
    n_tarjeta = forms.CharField(max_length=10)
    direccion = forms.CharField(max_length=40)
    