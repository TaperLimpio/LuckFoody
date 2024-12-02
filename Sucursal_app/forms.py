from django import forms
from Sucursal_app.models import Sucursal

#formulario para poder ingresar y actualizar sucursal
class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields=["nombre","direccion","fono","imagen"]