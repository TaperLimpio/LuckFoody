from typing import Any
from django import forms 
from Usuario_app.models import Usuario


#filtro de busqueda para encontrar ciertos tipos de usuarios
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

#formulario para ingresar usuario de tipo cliente
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'fono','contraseña']
        
        widgets={
            'contraseña':forms.TextInput(attrs={'type':'password'})
        }
    #evita ingresar un fono que no contenga numeros y "+"
    def clean_fono(self):
        fono = self.cleaned_data.get('fono')
        if not fono.startswith('+') or not fono[1:].replace(' ', '').isdigit():
            raise forms.ValidationError('El número de teléfono debe ser numérico y puede incluir un código de país con +.')
        return fono
    #evita ingresar un correro ya registrado y que no termine en "@gmail.com"
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError('El correo electrónico debe terminar en @gmail.com.')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado.')
        return email
    
    #evita crear una cuento con la misma contraseña
    def clean_contraseña(self):
        contraseña = self.cleaned_data.get('contraseña')
        if Usuario.objects.filter(contraseña=contraseña).exists():
            raise forms.ValidationError('Utilice otra contraseña.')
        return contraseña  

#formulario para crear cuentas por parte del administrador
class UsuarioAdminForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'fono', 'tipo','contraseña','ciudad']
        widgets={
            'contraseña':forms.TextInput(attrs={'type':'password'})
        }
    #permite no ingresar dos veces el mismo rut
    def clean_rut(self):
     rut = self.cleaned_data.get('rut')
     if Usuario.objects.filter(rut=rut).exists():
        raise forms.ValidationError('Este RUT ya está registrado.')

     return rut
    
    #evita ingresar un correro ya registrado y que no termine en "@gmail.com"
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError('El correo electrónico debe terminar en @gmail.com.')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado.')
        return email
    
    #evita crear una cuenta con la misma contraseña
    def clean_contraseña(self):
        contraseña = self.cleaned_data.get('contraseña')
        if Usuario.objects.filter(contraseña=contraseña).exists():
            raise forms.ValidationError('Utilice otra contraseña.')
        return contraseña     
    
    #permite solo el ingreso en "tipo" las palabras administrador y repartidor
    def clean_tipo(self):
        tipo = self.cleaned_data.get('tipo')
        if tipo not in ['administrador', 'repartidor']:
            raise forms.ValidationError('Tipo de usuario inválido.')
        return tipo
    
    #evita ingresar un fono que no contenga numeros y "+"
    def clean_fono(self):
        fono = self.cleaned_data.get('fono')
        if not fono.startswith('+') or not fono[1:].replace(' ', '').isdigit():
            raise forms.ValidationError('El número de teléfono debe ser numérico y puede incluir un código de país con +.')
        return fono