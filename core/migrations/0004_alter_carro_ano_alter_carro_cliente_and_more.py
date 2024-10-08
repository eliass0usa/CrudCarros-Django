# Generated by Django 5.1 on 2024-08-27 03:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_cliente_carro_ano_carro_cor_alter_carro_marca_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='ano',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='carro',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nascimento',
            field=models.IntegerField(default=''),
        ),
    ]
