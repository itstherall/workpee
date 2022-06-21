from django.db import models

# Create your models here.
class usuario(models.models):
    nome = models.CharField(max_length=255, blank=False, null=False)
    email = models.CharField(max_length=255, blank=False, null=False)
    senha = models.CharField(max_length=255, blank=False, null=False)