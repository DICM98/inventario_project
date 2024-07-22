from django.db import models
from reporte_tecnico.models import Reporte_Tecnico 

# Create your models here.
class Tipo_Movimiento(models.Model):
    motivo=models.TextField(max_length=200)
    fecha_creado=models.DateTimeField(auto_now_add=True)
    nombre_tipo=models.CharField(max_length=200)
    descripcion=models.TextField()
    responsable=models.CharField(max_length=100)
    reporte_tecnico= models.ForeignKey(Reporte_Tecnico,on_delete=models.CASCADE,null=False,blank=False,related_name='reporte_tecnico')