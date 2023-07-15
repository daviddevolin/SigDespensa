from django.forms import ModelForm
from .models import Categoria

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'