from django.forms import ModelForm
from .models import Item
from django import forms
from despensa.models import Despensa
from categoria.models import Categoria

class EmptyChoiceField(forms.ChoiceField):
    def __init__(self, empty_label='---------', *args, **kwargs):
        choices = [(None, empty_label)]
        super().__init__(choices=choices, *args, **kwargs)

class ItemForm(forms.ModelForm):
    despensa = forms.ModelChoiceField(queryset=Despensa.objects.all(), required=True)
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), required=True)

    class Meta:
        model = Item
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        despensa = cleaned_data.get('despensa')
        categoria = cleaned_data.get('categoria')

        if not despensa:
            self.add_error('despensa', 'Por favor, selecione uma despensa.')

        if not categoria:
            self.add_error('categoria', 'Por favor, selecione uma categoria.')

        return cleaned_data
