from django.db import models

class Despensa(models.Model):
    nome = models.CharField(max_length=100)
    quantTotal = models.IntegerField()
    capacidade = models.IntegerField()
    
    def __str__(self):
        return self.nome
