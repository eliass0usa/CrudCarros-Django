from django.db import models
  
class Cliente(models.Model):
  cpf = models.CharField(max_length=11, null=False, default="")
  nome = models.CharField(max_length=50, null=False, default="")
  sobrenome = models.CharField(max_length=100, null=False, default="") 
  nascimento = models.IntegerField(default="")

  def __str__(self):
    return self.nome

class Carro(models.Model):
  nome = models.CharField(max_length=50, null=False, default="")
  marca = models.CharField(max_length=100, null=False, default="")
  placa = models.CharField(max_length=8, null=False, default="")
  cor = models.CharField(max_length=20, null=False, default="")
  ano = models.IntegerField(null=False, default="")
  cliente = models.ForeignKey(to='core.Cliente', on_delete=models.CASCADE, null=True)
  
  def __str__(self):
    return '{} | {} | {}'.format(self.nome, self.marca, self.placa)