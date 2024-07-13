from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    carnet = models.TextField()
    edad = models.IntegerField()
    grupo = models.TextField()
    
    