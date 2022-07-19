from django.contrib import admin
from .models import Produto, Loja, Pedido

# Register your models here.
admin.site.register(Produto)
admin.site.register(Loja)
admin.site.register(Pedido)
