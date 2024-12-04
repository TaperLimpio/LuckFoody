from django import forms
from .models import Catalogo

#Formulario catalogo
class CatalogoForm(forms.ModelForm):
    class Meta:
        model = Catalogo
        fields = ['nombre', 'descripcion', 'imagen']

