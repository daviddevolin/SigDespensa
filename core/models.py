from django.db import models
from cpf_field.models import CPFField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = CPFField('cpf')
    telefone = models.CharField(max_length=11)
    
    def __str__(self):
        return self.user.first_name
    
@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwags):
    if created:
        Usuario.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user(sender, instance, **kwags):
    instance.usuario.save()