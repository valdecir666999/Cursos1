# Generated by Django 2.2.12 on 2022-11-26 01:20

import cpf_field.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome Completo')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('cpf', cpf_field.models.CPFField(max_length=14, verbose_name='cpf')),
            ],
        ),
        migrations.AlterField(
            model_name='cartao',
            name='ano',
            field=models.CharField(max_length=4, verbose_name='Ano'),
        ),
        migrations.AlterField(
            model_name='cartao',
            name='cvv',
            field=models.CharField(max_length=4, verbose_name='Codigo de Seguranca'),
        ),
        migrations.AlterField(
            model_name='cartao',
            name='mes',
            field=models.CharField(max_length=2, verbose_name='Mes'),
        ),
        migrations.AlterField(
            model_name='cartao',
            name='nome',
            field=models.CharField(max_length=50, verbose_name='Nome Completo'),
        ),
        migrations.AlterField(
            model_name='cartao',
            name='numeroCartao',
            field=models.CharField(max_length=16, verbose_name='Numero do Cartao'),
        ),
    ]
