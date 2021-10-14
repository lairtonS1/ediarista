from django.db import models

# Create your models here.


class Diarista(models.Model):
    nome_completo = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=12, null=False, blank= False)
    email = models.EmailField(null=False, blank=False)
    telefone = models.CharField(max_length=11, null=False, blank=False)
    lougradouro = models.CharField(max_length=60, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    bairro = models.CharField(max_length=30, null=False, blank=False)
    complemento = models.CharField(max_length=30, null=False, blank=True)
    cep = models.CharField(max_length=8, blank=False)
    estado = models.CharField(max_length=2, null=False, blank=False)
    codigo_ibge = models.IntegerField(null=False, blank=False)
    foto_usuario = models.ImageField(null=False, blank=False)
    objetos = models.Manager()