from django.db import models
from propiedad.models import Propiedad

# Create your models here.
class Local(models.Model):
    nombre=models.CharField(max_length=200)
    codigo=models.IntegerField()
    descripcion=models.TextField()
    responsable=models.TextField()
    propiedad = models.ForeignKey(Propiedad,on_delete=models.CASCADE,null=False,blank=False,related_name='propiedad')