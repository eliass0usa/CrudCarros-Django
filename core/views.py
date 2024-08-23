from django.shortcuts import render
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
