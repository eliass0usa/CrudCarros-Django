# Generated by Django 5.1 on 2024-08-23 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='marca',
            field=models.CharField(default='exemplo', max_length=100),
        ),
        migrations.AddField(
            model_name='carro',
            name='placa',
            field=models.CharField(default='exemplo', max_length=8),
        ),
        migrations.AlterField(
            model_name='carro',
            name='nome',
            field=models.CharField(default='exemplo', max_length=50),
        ),
    ]
