from django.db import models
from rol.models import Rol

# Create your models here.
class Usuario(models.Model):
  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50)
  nombre_usuario= models.CharField(max_length=50)
  contrasena= models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  fecha_crado = models.DateTimeField(auto_now_add=True)
  fecha_actualizado =  models.DateTimeField(auto_now_add=True)
  telf = models.CharField(max_length=50)
  rol = models.ManyToManyField(Rol,related_name='rol')