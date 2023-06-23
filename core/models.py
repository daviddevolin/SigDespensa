from django.db import models
from cpf_field.models import CPFField
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class Usuario(AbstractUser):
    cpf = CPFField('cpf')
    telefone = models.CharField(max_length=11)
    
    def __str__(self):
        return self.user.first_name
    
@receiver(post_save, sender=Usuario)
def create_usuario(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(user=instance)

@receiver(post_save, sender=Usuario)
def save_usuario(sender, instance, **kwargs):
    instance.save()