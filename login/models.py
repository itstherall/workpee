from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=255, choices=[
                            ('Vendedor', 'Vendedor'), ('Comprador', 'Comprador')])

    def __str__(self):
        return self.user.username
