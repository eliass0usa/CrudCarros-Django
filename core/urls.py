from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('carros', views.homeCarros, name="homeCarros"),
    path('salvar/', views.salvar, name="salvar"),
    path('editar/<int:id>', views.editar, name="editar"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete")
]