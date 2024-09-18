from django import forms
from .models import Cliente, Carro
from django.contrib.auth.models import User
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
    
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password']
        widgets = {'password': forms.PasswordInput()}
        
    def clena(self):
        cleaned_data = super().clean
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            raise forms.ValidationError("As senhas não correspondem")
        
        return cleaned_data
        
class CustomLoginForm(AuthenticationForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    