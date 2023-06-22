from django.forms import ModelForm
from .models import Usuario
from django.contrib.auth.models import User

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['cpf', 'telefone']
class UserForm(ModelForm):
    class Meta:
        
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
