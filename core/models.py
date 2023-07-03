from django.db import models
from cpf_field.models import CPFField
from django.contrib.auth.models import AbstractUser
from despensa.models import Despensa


class Usuario(AbstractUser):
    cpf = CPFField('cpf')
    telefone = models.CharField(max_length=11)
    despensas = models.ManyToManyField(Despensa, blank=True)

    def __str__(self):
        return self.first_name
