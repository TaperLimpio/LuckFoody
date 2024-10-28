from django import forms
from Sucursal_app.models import Sucursal

class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields="__all__"