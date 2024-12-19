from django import forms
from .models import Catalogo

#Formulario catalogo
class CatalogoForm(forms.ModelForm):
    class Meta:
        model = Catalogo
        fields = ['nombre', 'descripcion', 'imagen']
        widgets ={
            'nombre':forms.TextInput(attrs={'class':'form-control'})
        }
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        nombre_anterior = Catalogo.objects.get(id = self.instance.id).nombre
        if nombre != nombre_anterior:
            if Catalogo.objects.filter(nombre=nombre).exists():
                raise forms.ValidationError('Este nombre ya está registrado. Elija un nombre diferente.')
        return nombre

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        descripcion_anterior = Catalogo.objects.get(id = self.instance.id).descripcion
        if descripcion != descripcion_anterior:
            if Catalogo.objects.filter(descripcion=descripcion).exists():
                raise forms.ValidationError('Esta descripción ya está registrada. Elija una descripción diferente.')
        return descripcion
