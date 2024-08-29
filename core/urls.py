from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    # Clientes
    path('clientes', views.homeClientes, name="homeClientes"),
    path('salvarcliente', views.salvarCliente, name="salvarCliente"),
    path('deletarCliente<int:id>', views.deletarCliente, name="deletarCliente"),
    path('clientes', views.homeClientes, name="homeClientes"),
    
    # Carros
    path('carros', views.homeCarros, name="homeCarros"),
    path('salvar/', views.salvar, name="salvar"),
    path('editar/<int:id>', views.editar, name="editar"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete")
]