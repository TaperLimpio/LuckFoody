from typing import Any
from django import forms 
from Usuario_app.models import Usuario

FILTRO_DECICIONES_1=(
    ('Todo','----'),
    ('Administrador','administrador'),
    ('Usuario','usuario'),
    ('Repartidor','repartidor')
)

FILTRO_DECICIONES_2=(
    ('Todo','----'),
    ('Activo','activo'),
    ('Inactivo','inactivo')
)


class Filtro(forms.Form):
    tipo = forms.ChoiceField(choices=FILTRO_DECICIONES_1)
    estado = forms.ChoiceField(choices=FILTRO_DECICIONES_2)

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'fono','contraseña']
    def clean_fono(self):
        fono = self.cleaned_data.get('fono')
        if not fono.startswith('+') or not fono[1:].replace(' ', '').isdigit():
            raise forms.ValidationError('El número de teléfono debe ser numérico y puede incluir un código de país con +.')
        return fono

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError('El correo electrónico debe terminar en @gmail.com.')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado.')
        return email
    
    def clean_nombre(self):
        nombre= self.cleaned_data.get('nombre')
        if Usuario.objects.filter(nombre=nombre).exists():
             raise forms.ValidationError('utilize otro nombre')
        return nombre

class UsuarioAdminForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'fono', 'tipo','contraseña']

    def clean_rut(self):
     rut = self.cleaned_data.get('rut')
     if Usuario.objects.filter(rut=rut).exists():
        raise forms.ValidationError('Este RUT ya está registrado.')

     return rut
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError('El correo electrónico debe terminar en @gmail.com.')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado.')
        return email

    def clean_nombre(self):
        nombre= self.cleaned_data.get('nombre')
        if Usuario.objects.filter(nombre=nombre).exists():
             raise forms.ValidationError('utilize otro nombre')
        return nombre    
    
    def clean_tipo(self):
        tipo = self.cleaned_data.get('tipo')
        if tipo not in ['administrador', 'repartidor']:
            raise forms.ValidationError('Tipo de usuario inválido.')
        return tipo
    def clean_fono(self):
        fono = self.cleaned_data.get('fono')
        if not fono.startswith('+') or not fono[1:].replace(' ', '').isdigit():
            raise forms.ValidationError('El número de teléfono debe ser numérico y puede incluir un código de país con +.')
        return fono