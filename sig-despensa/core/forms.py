from django import forms
from django.forms import ModelForm, ValidationError, PasswordInput
from .models import Usuario
from django.contrib.auth import password_validation

class UsuarioForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'cpf', 'telefone']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = PasswordInput()
        self.fields['confirm_password'].widget = PasswordInput()

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        print(confirm_password, password)
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("As senhas não correspondem.")
        
        try:
            password_validation.validate_password(password)
        except forms.ValidationError as validation_error:
            self.add_error('password', validation_error)

        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        print('trying to add:', username)

        if self.check_user_exists(username):
            raise ValidationError(f"Nome de usuário {username} já existe", 'invalid')
        return username

    def check_user_exists(self, username):
        try:
            Usuario.objects.get(username=username)
            return True
        except Usuario.DoesNotExist:
            return False
