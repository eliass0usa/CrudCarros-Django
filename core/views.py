from django.shortcuts import render, redirect, get_object_or_404
from .models import Carro, Cliente

# HOME
def home(request):
  return render (request, "index.html")

# MODEL CLIENTE #
def homeClientes(request):
  clientes = Cliente.objects.all()
  return render (request, "clientes.html", {'clientes': clientes})

def salvarCliente(request):
  clicpf = request.POST.get("cpf")
  clinome = request.POST.get("nome")
  clisobrenome = request.POST.get("sobrenome")
  clinascimento = request.POST.get("nascimento")
  Cliente.objects.create(cpf=clicpf, nome=clinome, sobrenome=clisobrenome, nascimento=clinascimento)
  clientes = Cliente.objects.all()
  return render(request, "carros.html", {'clientes': clientes})

def deletarCliente(request, id):
  cliente = get_object_or_404(Cliente, id=id)
  cliente.delete()
  return redirect(homeClientes)

# MODEL CARROS #
def homeCarros(request):
  carros = Carro.objects.all()
  return render (request, "carros.html", {'carros': carros})

def salvar(request):
  cnome = request.POST.get("nome")
  cmarca = request.POST.get("marca")
  cplaca = request.POST.get("placa")
  ccor = request.POST.get("cor")
  cano = request.POST.get("ano")
  Carro.objects.create(nome=cnome, marca=cmarca, placa=cplaca, cor=ccor, ano=cano)
  carros = Carro.objects.all()
  return render(request, "carros.html", {'carros':carros})

def editar(request, id):
  carro = get_object_or_404(Carro, id=id)
  return render(request, "update.html", {"carro":carro})

def update(request, id):
  carro = get_object_or_404(Carro, id=id)
  
  if request.method == 'POST':
    cnome = request.POST.get("nome")
    cmarca = request.POST.get("marca")
    cplaca = request.POST.get("placa")
    ccor = request.POST.get("cor") 
    cano = request.POST.get("ano")
    if cnome and cmarca and cplaca and ccor and cano:
      carro.nome = cnome
      carro.marca = cmarca
      carro.placa = cplaca
      carro.cor = ccor
      carro.ano = cano
      carro.save()
      return redirect('homeCarros')
    else:
      return render(request, "update.html", {"carro": carro, "error": "Todos os campos são obrigatórios"})
     
  return render(request, "update.html", {"carro":carro})


def delete(request, id):
  carro = get_object_or_404(Carro, id=id)
  carro.delete()
  return redirect(homeCarros)