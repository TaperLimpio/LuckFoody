from django import forms
from .models import Platillo
from Sucursal_app.models import Sucursal

#formulario de platillo
class PlatilloForm(forms.ModelForm):
    class Meta:
        model = Platillo
        fields = ['nombre', 'codigo', 'precio', 'descripcion', 'imagen', 'sucursales', 'catalogo']
    #filtra las sucursales para que solo puedas enlazar platillo con sucursales activas 
    def __init__(self, *args, **kwargs):
        super(PlatilloForm, self).__init__(*args, **kwargs)
        self.fields['sucursales'].queryset = Sucursal.objects.filter(estado='activo')
    
    #evita ingresar dos veces un platillo con el mismo nombre
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if Platillo.objects.filter(nombre=nombre).exists():
            raise forms.ValidationError('Este nombre ya está registrado. Elija un nombre diferente.')
        return nombre
    
    #evita ingresar dos veces un platillo con el mismo codigo 
    def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo')
        if Platillo.objects.filter(codigo=codigo).exists():
            raise forms.ValidationError('Este código ya está registrado. Elija un código diferente.')
        return codigo