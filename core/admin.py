from django.contrib import admin
from .models import Cliente, Carro, User

admin.site.register(Carro)
admin.site.register(Cliente)
admin.site.register(User)