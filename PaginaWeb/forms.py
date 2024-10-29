from typing import Any
from django import forms 
from PaginaWeb.models import Usuario



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
        return email
    
    def clean_contraseña(self):
        contraseña= self.cleaned_data.get('contraseña')
        if Usuario.objects.filter(contraseña=contraseña).exists():
             raise forms.ValidationError('utilize otra contraseña')
        return contraseña

class UsuarioAdminForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'fono', 'tipo','contraseña']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError('El correo electrónico debe terminar en @gmail.com.')
        return email

    def clean_contraseña(self):
        contraseña= self.cleaned_data.get('contraseña')
        if Usuario.objects.filter(contraseña=contraseña).exists():
             raise forms.ValidationError('utilize otra contraseña')
        return contraseña    
    
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