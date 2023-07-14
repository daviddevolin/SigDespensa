from django.forms import ModelForm
from .models import Despensa

class DespensaForm(ModelForm):
    class Meta:
        model = Despensa
        fields = '__all__'

from typing import Any, Dict
from django.forms import ModelForm, ValidationError
from .models import Despensa

class DespensaForm(ModelForm):
    class Meta:
        model = Despensa
        fields = [ 'nome', 'usuarios']

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        print('trying to add:', nome)

        if (self.check_despensa_exists(nome)):
            raise ValidationError(f"Nome de Despensa {nome} já existe", 'invalid')
        return nome
    
    def check_despensa_exists(self, nome):
        try:
            Despensa.objects.get(nome=nome)
            return True
        except Despensa.DoesNotExist:
            return False


