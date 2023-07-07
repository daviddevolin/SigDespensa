from typing import Any, Dict
from django.forms import ModelForm, ValidationError, PasswordInput
from .models import Usuario
from django import forms

class UsuarioForm(ModelForm):

    class Meta:
        model = Usuario
        fields = [ 'username', 'first_name', 'last_name', 'email', 'password','cpf', 'telefone',]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Alterar o tipo de campo para password
        self.fields['password'].widget = PasswordInput()

    def clean_username(self):
        username = self.cleaned_data.get('username')
        print('trying to add:', username)

        if (self.check_user_exists(username)):
            raise ValidationError(f"Nome de usuário {username} já existe", 'invalid')
        return username
    
    def check_user_exists(self, username):
        try:
            Usuario.objects.get(username=username)
            return True
        except Usuario.DoesNotExist:
            return False