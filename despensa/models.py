from django.db import models
from core.models import Usuario

class Despensa(models.Model):
    nome = models.CharField(max_length=100)
    quantTotal = models.IntegerField(default=0, null=True)


    usuarios = models.ManyToManyField(Usuario, blank=True)
    
    def __str__(self):
        return self.nome
