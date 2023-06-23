from django.forms import ModelForm
from .models import Usuario
from django.contrib.auth.models import User

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = [ 'username', 'first_name', 'last_name', 'email', 'password','cpf', 'telefone',]

