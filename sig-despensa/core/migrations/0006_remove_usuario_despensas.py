# Generated by Django 4.2.1 on 2023-07-05 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_usuario_despensas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='despensas',
        ),
    ]
