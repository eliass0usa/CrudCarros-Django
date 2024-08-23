from django.db import models

class Carro(models.Model):
  nome = models.CharField(max_length=50, null=False, default="exemplo")
  marca = models.CharField(max_length=100, null=False, default="exemplo")
  placa = models.CharField(max_length=8, null=False, default="exemplo")
  
  def __str__(self):
    return "{} | {} | {}".format(self.nome, self.marca, self.placa)
  
  