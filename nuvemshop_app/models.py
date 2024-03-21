from django.db import models

# Create your models here.


class Integracao(models.Model):
    nome_loja = models.CharField(max_length=100)
    telefone_loja = models.CharField(max_length=20)
    cnpj_cpf_loja = models.CharField(max_length=14)
    autorization_token = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.autorization_token



class Cliente(models.Model):
    cpf_cnpj = models.CharField(max_length=14)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.nome


class Venda(models.Model):
    id_venda = models.CharField(max_length=20, primary_key=True)
    data = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    status_pagamento = models.CharField(max_length=50)
    status_envio = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.cliente.nome
