from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    categoria = models.CharField(max_length= 50)
    
    def __str__(self) -> str:
        return self.categoria
    
class Contato(models.Model):
    nome = models.CharField(max_length= 50)
    sobrenome = models.CharField(max_length= 50, blank= True)
    telefone = models.CharField(max_length= 20)
    email = models.EmailField(max_length= 50, blank=True)
    data_criacao = models.DateTimeField(default= timezone.now)
    descricao = models.TextField(blank= True)
    categoria = models.ForeignKey(Categoria, on_delete= models.DO_NOTHING)
    mostrar = models.BooleanField(default= True)
    
    def __str__(self) -> str:
        return self.nome