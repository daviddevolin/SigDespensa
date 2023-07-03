from django.db import models

from item.models import Item
# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome