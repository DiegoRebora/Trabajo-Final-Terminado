from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Jugadores(models.Model):
    nombre =  models.CharField(max_length=64)
    apellido =  models.CharField(max_length=64)
    nacionalidad =  models.CharField(max_length=64)
    edad = models.IntegerField()
    circuito = models.CharField(max_length=64)
    marca = models.CharField(max_length=64, blank=True)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

class Circuito(models.Model):
    nombre = models.CharField(max_length=64)
    alcance = models.CharField(max_length=64)
    ranking_premios = models.IntegerField()
    cant_torneos = models.IntegerField(null=True, blank=True)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    
    def __str__(self):
        return f"{self.nombre} | {self.alcance}"
    

class Marca(models.Model):
    nombre = models.CharField(max_length=64)
    origen = models.CharField(max_length=64)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre}"
 