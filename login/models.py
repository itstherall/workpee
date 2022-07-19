from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=255, choices=[
                            ('Vendedor', 'Vendedor'), ('Comprador', 'Comprador')])

    def __str__(self):
        return self.user.username


class Loja(models.Model):
    nome = models.CharField(max_length=255, blank=True, null=True, default='')
    descricao = models.TextField(default="Nova loja")

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=255, blank=True, null=True, default='')
    preco = models.FloatField()
    descricao = models.TextField()
    imagem = models.FileField(upload_to='produtos/')
    loja = models.ForeignKey(Loja, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    quantidade = models.IntegerField()
    produto = models.ForeignKey(
        Produto, on_delete=models.SET_DEFAULT, default='')
    customizacao = models.TextField()

    def __str__(self):
        return self.produto.nome + ', quantidade:' + str(self.quantidade)
