from django.contrib import admin
from django.urls import path, include
from .views import salvar, editar, update, delete, home

urlpatterns = [
    path('', home, name="home"),
    path('salvar/', salvar, name="salvar"),
    path('editar/<int:id>', editar, name="editar"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
]