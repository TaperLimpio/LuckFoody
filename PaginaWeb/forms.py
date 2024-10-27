from django import forms 
from PaginaWeb.models import Usuario



class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'fono','contraseña']


class UsuarioAdminForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'fono', 'tipo','contraseña']
    def clean_tipo(self):
        tipo = self.cleaned_data.get('tipo')
        if tipo not in ['administrador', 'repartidor']:
            raise forms.ValidationError('Tipo de usuario inválido.')
        return tipo
