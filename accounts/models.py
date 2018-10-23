from django.db import models
from django.contrib.auth.models import User
from accounts.models import *


class Usuario(models.Model):

    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=30, unique=True)
    data_nascimento = models.DateField(null=True)
    logradouro = models.CharField(max_length=90, null=True, blank=True)
    numero = models.CharField(max_length=20, null=True, blank=True)
    cep = models.CharField(max_length=9, null=True, blank=True)
    complemento = models.CharField(max_length=20, null=True, blank=True)
    bairro = models.CharField(max_length=20, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    nome_mae = models.CharField(max_length=120,null=True,blank=True)
    nome_pai = models.CharField(max_length=120,null=True,blank=True)
    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    def __str__(self):
        return self.Nome
