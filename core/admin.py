from django.contrib import admin
from .models import Cliente, Carro

admin.site.register(Carro)
admin.site.register(Cliente)