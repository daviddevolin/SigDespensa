from django.forms import ModelForm
from .models import Usuario
class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'cpf', 'telefone']