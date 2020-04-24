from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator,EmailValidator

class Archivo(models.Model):
    nombre = models.TextField(max_length=50)
    tamano = models.TextField(max_length=30)
    fecha = models.DateTimeField(auto_now_add= True)
    ubicacion = models.TextField(max_length=254)
    #numSongs = models.IntegerField(default=0,validators=[MinValueValidator(0,"Year must not surpass 1990"),MaxValueValidator(12400,"Year cannot be greater than 2056")])

