from django.db import models
from cpf_field.models import CPFField


class Cartao(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome Completo")
    email = models.CharField(max_length=50, verbose_name="Email")
    cpf = CPFField('cpf')
    numeroCartao = models.CharField(max_length=16, verbose_name="Numero do Cartao")
    mes = models.CharField(max_length=2, verbose_name="Mes")
    ano = models.CharField(max_length=4, verbose_name="Ano")
    cvv = models.CharField(max_length=4, verbose_name="Codigo de Seguranca")
    
    def __str__(self):
        return "{} ({})".format(self.nome, self.email,self.cpf, self.numeroCartao, self.mes, self.ano, self.cvv)
    

class Pix(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome Completo")
    email = models.CharField(max_length=50, verbose_name="Email")
    cpf = CPFField('cpf')

    def __str__(self):
        return "{} ({})".format(self.nome, self.email, self.cpf)
    



   


