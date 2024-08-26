from django.shortcuts import render, redirect
from .models import Carro

def home(request):
  carros = Carro.objects.all()
  return render (request, "index.html", {'carros': carros})

def salvar(request):
  cnome = request.POST.get("nome")
  cmarca = request.POST.get("marca")
  cplaca = request.POST.get("placa")
  Carro.objects.create(nome=cnome, marca=cmarca, placa=cplaca)
  carros = Carro.objects.all()
  return render(request, "index.html", {'carros':carros})

def editar(request, id):
  carro = Carro.objects.get(id=id)
  return render(request, "update.html", {"carro":carro})

def update(request, id):
  cnome = request.POST.get("nome")
  cmarca = request.POST.get("marca")
  cplaca = request.POST.get("placa")
  carro = Carro.objects.get(id=id)
  
  carro.nome = cnome
  carro.marca = cmarca
  carro.placa = cplaca
  carro.save()
  return redirect(home)

def delete(request, id):
  carro = Carro.objects.get(id=id)
  carro.delete()
  return redirect(home)