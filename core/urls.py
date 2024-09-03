from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    
    # Clientes
    path('homeClientes', views.homeClientes, name="homeClientes"),
    path('salvarcliente', views.salvarCliente, name="salvarCliente"),   
    path('deletarCliente<int:id>', views.deletarCliente, name="deletarCliente"),
    path('editarCliente<int:id>', views.editarCliente, name="editarCliente"),
    
    # Carros
    path('carros', views.homeCarros, name="homeCarros"),
    path('salvar/', views.salvar, name="salvar"),
    path('editar/<int:id>', views.editar, name="editar"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete")
]