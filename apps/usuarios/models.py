from django.db import models

class Usuario(models.Model):
    userId = models.AutoField(primary_key=True, unique=True)
    nome_user = models.CharField(max_length=20)
    sobrenome_user = models.CharField(max_length=70)
