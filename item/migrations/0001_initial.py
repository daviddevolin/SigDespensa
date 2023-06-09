# Generated by Django 4.2.1 on 2023-05-27 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_id', models.CharField(max_length=50)),
                ('nome', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=8)),
                ('data_validade', models.DateField()),
            ],
        ),
    ]
