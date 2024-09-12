from django import forms
from .models import Cliente, Carro
from django.contrib.auth.models import UserManager, User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cpf', 'nome', 'sobrenome', 'nascimento']
        widgets = {
            'nascimento': forms.DateInput(attrs={'type': 'date'}),
        }

class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ['nome', 'marca', 'placa', 'cor', 'ano']
        
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    
class RegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password' ]
        widgets = {'password': forms.PasswordInput()}