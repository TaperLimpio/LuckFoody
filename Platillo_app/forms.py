from django import forms
from .models import Platillo
from Sucursal_app.models import Sucursal

class PlatilloForm(forms.ModelForm):
    class Meta:
        model = Platillo
        fields = ['nombre', 'codigo', 'precio', 'descripcion', 'imagen', 'sucursales', 'catalogo']

    def init(self, args, **kwargs):
        super(PlatilloForm, self).init(args, **kwargs)
        self.fields['sucursales'].queryset = Sucursal.objects.filter(estado='activo')

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if Platillo.objects.filter(nombre=nombre).exists():
            raise forms.ValidationError('Este nombre ya está registrado. Elija un nombre diferente.')
        return nombre

    def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo')
        if Platillo.objects.filter(codigo=codigo).exists():
            raise forms.ValidationError('Este código ya está registrado. Elija un código diferente.')
        return codigo