from django.db import models
from usuario.models import Usuario

# Create your models here.
class Area_Responsable(models.Model):
     nombre=models.CharField(max_length=200)
     responsable_salida=models.CharField(max_length=200)
     responsable_entrada=models.CharField(max_length=200)
     fecha_creada=models.DateTimeField(auto_now_add=True)
     usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE,null=False,blank=False,related_name='usuario')