from django.db import models

class Item(models.Model):
    codigo_id = models.CharField(max_length=50)
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    peso = models.DecimalField(max_digits=8, decimal_places=2)
    data_validade = models.DateField()
    
    def __str__(self):
        return self.nome
