from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=255, choices=[
                            ('Vendedor', 'Vendedor'), ('Comprador', 'Comprador')])

    def __str__(self):
        return self.user.username


class Produto(models.Model):
    nome = models.CharField(max_length=255, blank=True, null=True, default='')
    preco = models.FloatField()
    descricao = models.TextField()
    imagem = models.FileField(upload_to='produtos/%Y/%m/%d/%H/%M')
    # usuario = models.ForeignKey(User, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome
