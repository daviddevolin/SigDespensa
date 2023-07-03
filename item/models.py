from django.db import models

from despensa.models import Despensa

class Item(models.Model):
    nome = models.CharField(max_length=100)
    categoria_item = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    peso = models.DecimalField(max_digits=8, decimal_places=2)
    data_validade = models.DateField()
    despensa = models.ForeignKey(Despensa, on_delete=models.CASCADE, related_name='itens')
    
    def __str__(self):
        return self.nome
