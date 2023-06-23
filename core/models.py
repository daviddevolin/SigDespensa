from django.db import models
from cpf_field.models import CPFField
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class Usuario(AbstractUser):
    cpf = CPFField('cpf')
    telefone = models.CharField(max_length=11)
    
    def __str__(self):
        return self.first_name
