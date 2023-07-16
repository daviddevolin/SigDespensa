from django.db import models
from cpf_field.models import CPFField
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    cpf = CPFField('cpf')
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return self.first_name
