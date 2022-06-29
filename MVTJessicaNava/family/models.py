from errno import EDEADLK
from django.db import models

# Create your models here.
class familia_nava(models.Model):
    nombre=models.CharField(max_length=40)
    parentesco=models.CharField(max_length=20)
    nacimiento=models.DateField()
    edad=models.IntegerField()

class ubicacion(models.Model):
    direccion=models.CharField(max_length=60)
    colonia=models.CharField(max_length=60)
    CP=models.IntegerField()

class hobbies(models.Model):
    nombre=models.CharField(max_length=60)
    horas_sem=models.IntegerField()