from typing import Any
from django import forms 
from Usuario_app.models import Usuario
from django.contrib.auth.hashers import check_password,make_password

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

tipos_de_usuario=(
    ('administrador','administrador'),
    ('repartidor','repartidor')
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
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'fono':forms.TextInput(attrs={'class':'form-control'}),
            'contraseña':forms.TextInput(attrs={'type':'password','class':'form-control'})
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
    
    #evita crear una cuenta con el mismo nombre
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if Usuario.objects.filter(nombre=nombre).exists():
            raise forms.ValidationError('Utilice otro nombre.')
        return nombre 
    
#formulario para crear cuentas por parte del administrador
class UsuarioAdminForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'fono', 'tipo','contraseña','ciudad']
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'fono':forms.TextInput(attrs={'class':'form-control'}),
            'tipo':forms.Select(choices=tipos_de_usuario, attrs={'class':'form-select'}),
            'contraseña':forms.TextInput(attrs={'type':'password','class':'form-control'}),
            'ciudad':forms.TextInput(attrs={'class':'form-control'}),
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

        #evita crear una cuenta con el mismo nombre
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if Usuario.objects.filter(nombre=nombre).exists():
            raise forms.ValidationError('Utilice otro nombre.')
        return nombre   
    
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
    
#formulario para ingresar usuario de tipo cliente
class ActualizarUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'fono','ciudad']
        
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'fono':forms.TextInput(attrs={'class':'form-control'}),
            'ciudad':forms.TextInput(attrs={'class':'form-control'}),
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
    
    #evita crear una cuenta con el mismo nombre
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        nombre_anterior = Usuario.objects.get(id = self.instance.id).nombre
        if nombre != nombre_anterior:
            if Usuario.objects.filter(nombre=nombre).exists():
                raise forms.ValidationError('Utilice otro nombre.')
        return nombre  

class ActualizarContraseñaUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['contraseña']
        widgets={
            'contraseña':forms.TextInput(attrs={'class':'form-control'})
        }
    contraseña_nueva = forms.CharField(max_length=76,widget=forms.TextInput(attrs={'class':'form-control'}))

    def clean_contraseña(self):
        contraseña = self.cleaned_data.get('contraseña')
        contraseña_anterior = Usuario.objects.get(id = self.instance.id).contraseña

        print(self.cleaned_data.get('contraseña_nueva'))
        if check_password(contraseña,contraseña_anterior):
            raise forms.ValidationError('Ingreso la misma contraseña')
        return contraseña
    
#formulario para actualizar cuentas por parte del administrador
class ActualizarUsuarioAdminForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'fono','ciudad']
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'fono':forms.TextInput(attrs={'class':'form-control'}),
            'ciudad':forms.TextInput(attrs={'class':'form-control'}),
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
        email_anterior = Usuario.objects.get(id = self.instance.id).email
        if email != email_anterior:
            if not email.endswith('@gmail.com'):
                raise forms.ValidationError('El correo electrónico debe terminar en @gmail.com.')
            if Usuario.objects.filter(email=email).exists():
                raise forms.ValidationError('Este correo electrónico ya está registrado.')
        return email

    #evita crear una cuenta con el mismo nombre
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        nombre_anterior = Usuario.objects.get(id = self.instance.id).nombre
        if nombre != nombre_anterior:
            if Usuario.objects.filter(nombre=nombre).exists():
                raise forms.ValidationError('Utilice otro nombre.')
        return nombre   
    
    #evita ingresar un fono que no contenga numeros y "+"
    def clean_fono(self):
        fono = self.cleaned_data.get('fono')
        if not fono.startswith('+') or not fono[1:].replace(' ', '').isdigit():
            raise forms.ValidationError('El número de teléfono debe ser numérico y puede incluir un código de país con +.')
        return fono