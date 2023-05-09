from django.db import models
from cpf_field.models import CPFField
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    #senha = models.CharField(max_length=50),
    cpf = CPFField('cpf')
    telefone = models.CharField(max_length=11)
    
    def __str__(self):
        return self.nome
