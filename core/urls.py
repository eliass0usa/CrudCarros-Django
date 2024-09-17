from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from .forms import CustomLoginForm

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', auth_views.LoginView.as_view(authentication_form=CustomLoginForm ,template_name='registration/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),    
    path('signUp/',views.signUp, name='signUp'),
    
    # Senhas
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    
    # Clientes
    path('homeClientes', views.homeClientes, name="homeClientes"),
    path('salvarcliente', views.salvarCliente, name="salvarCliente"),   
    path('deletarCliente<int:id>', views.deletarCliente, name="deletarCliente"),
    path('editarCliente<int:id>', views.editarCliente, name="editarCliente"),
    
    # Carros
    path('carros', views.homeCarros, name="homeCarros"),
    path('salvar/', views.salvar, name="salvar"),
    path('editarCarro/<int:id>', views.editarCarro, name="editarCarro"),
    path('delete/<int:id>', views.delete, name="delete")
]