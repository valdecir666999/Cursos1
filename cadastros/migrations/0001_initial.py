# Generated by Django 2.2.12 on 2022-11-25 02:20

import cpf_field.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cartao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('cpf', cpf_field.models.CPFField(max_length=14, verbose_name='cpf')),
                ('numeroCartao', models.IntegerField()),
                ('mes', models.CharField(max_length=2)),
                ('ano', models.CharField(max_length=4)),
                ('cvv', models.CharField(max_length=4)),
            ],
        ),
    ]