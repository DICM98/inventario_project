from django.db import models
from rol.models import Rol

# Create your models here.
class Usuario(models.Model):
  name = models.CharField(max_length=50)
  surname = models.CharField(max_length=50)
  username= models.CharField(max_length=50)
  password= models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  update_at =  models.DateTimeField(auto_now_add=True)
  phone = models.CharField(max_length=50)
  rol = models.ManyToManyField(Rol,related_name='rol')