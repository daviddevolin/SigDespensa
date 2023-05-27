from django.db import models

class Despensa(models.Model):
    nome = models.CharField(max_length=100)
    quantTotal = models.IntegerField()
    capacidade = models.IntegerField()
    categoria = models.CharField(max_length=50)
    def __str__(self):
        return self.nome
