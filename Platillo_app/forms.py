
from django import forms
from .models import Platillo

FILTRO_DECICIONES_1=(
    ('Todo','----'),
    ('activo','activo'),
    ('inactivo','inactivo'),
    ('tomado','tomado'),
    ('entregado','entregado')
)

class FiltroPlatillo(forms.Form):
    estado = forms.ChoiceField(choices=FILTRO_DECICIONES_1)
    
class PlatilloForm(forms.Form):
    n_tarjeta = forms.CharField(max_length=10)
    direccion = forms.CharField(max_length=40)