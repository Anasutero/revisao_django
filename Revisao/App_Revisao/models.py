from django.db import models

# Create your models here.

class Pessoas(models.Model):
    nome = models.CharField(max_length=120)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome
