from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=60)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=20)
    rua = models.CharField(max_length=60)
    bairro = models.CharField(max_length=20)
    cidade = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    cep = models.CharField(max_length=8)
    login = models.OneToOneField("Login", on_delete=models.PROTECT, blank=True, null=True) # Relação 1 para 1

class Login(models.Model):
    login = models.CharField(max_length=20)
    senha = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

class Produto(models.Model):
    nomeprod = models.CharField(max_length=60)
    quantidadedisp = models.IntegerField()
    valor = models.FloatField()

    def __str__(self) -> str:
        return self.nomeprod
    
class Frete(models.Model):
    destino = models.CharField(max_length=60)
    valorfrete = models.FloatField()
    formapagamento = models.CharField(max_length=20)


class Compra(models.Model):
    valorcompra = models.FloatField()
    formapagamento = models.CharField(max_length=20)
    quantidade = models.IntegerField()
    login = models.OneToOneField("Frete", on_delete=models.PROTECT, blank=True, null=True)  # Relação 1 para 1
    produto = models.ForeignKey("Produto", on_delete=models.PROTECT, blank=True, null=True) # Relação 1 para N