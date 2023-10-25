from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=256,unique=True)


class Evento(models.Model):
    
    nome = models.CharField(max_length=256) 
    categoria = models.ForeignKey("categoria", on_delete=models.SET_NULL,null=True)
    local = models.CharField(max_length=256, blank=True)
    link =  models.CharField(max_length=256, blank=True)
