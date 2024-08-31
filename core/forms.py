from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cpf', 'nome', 'sobrenome', 'nascimento']
        widgets = {
            'nascimento': forms.DateInput(attrs={'type': 'date'}),
        }
