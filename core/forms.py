from django.forms import ModelForm
from .models import Usuario


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = [ 'username', 'first_name', 'last_name', 'email', 'password','cpf', 'telefone',]

