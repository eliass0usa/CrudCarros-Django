from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import *
from .forms import ClienteForm, CarroForm, RegistrationForm
from .models import Carro, Cliente

# HOME
def home(request):
    return render(request, "index.html")

# SIGN UP
def signUp(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            auth_login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, "registration/signUp.html", {'form': form})

def passwordReset(request):
    return render('registration/passwordReset.html')  

# MODEL CLIENTE #
def homeClientes(request):
    clientes = Cliente.objects.all()
    return render(request, "clientes.html", {'clientes': clientes})

def salvarCliente(request):
    clicpf = request.POST.get("cpf")
    clinome = request.POST.get("nome")
    clisobrenome = request.POST.get("sobrenome")
    clinascimento = request.POST.get("nascimento")
    Cliente.objects.create(cpf=clicpf, nome=clinome, sobrenome=clisobrenome, nascimento=clinascimento)
    clientes = Cliente.objects.all()
    return render(request, "clientes.html", {'clientes': clientes})

def deletarCliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return redirect(homeClientes)

def editarCliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('homeClientes')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'editar_cliente.html', {'form': form, 'cliente': cliente})

# MODEL CARROS #
def homeCarros(request):
    carros = Carro.objects.all()
    return render(request, "carros.html", {'carros': carros})

def salvar(request):
    cnome = request.POST.get("nome")
    cmarca = request.POST.get("marca")
    cplaca = request.POST.get("placa")
    ccor = request.POST.get("cor")
    cano = request.POST.get("ano")
    Carro.objects.create(nome=cnome, marca=cmarca, placa=cplaca, cor=ccor, ano=cano)
    carros = Carro.objects.all()
    return render(request, "carros.html", {'carros': carros})

def editarCarro(request, id):
    carro = get_object_or_404(Carro, id=id)

    if request.method == 'POST':
        form = CarroForm(request.POST, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('homeCarros')
    else:
        form = CarroForm(instance=carro)
    return render(request, 'editar_carro.html', {'form': form, 'carro': carro})

def delete(request, id):
    carro = get_object_or_404(Carro, id=id)
    carro.delete()
    return redirect(homeCarros)
