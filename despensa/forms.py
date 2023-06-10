from django.forms import ModelForm
from .models import Despensa

class DespensaForm(ModelForm):
    class Meta:
        model = Despensa
        fields = '__all__'