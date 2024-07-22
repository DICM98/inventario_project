from django.db import models
from area_responsable.models import Area_Responsable
from local.models import Local
from tipo_movimiento.models import  Tipo_Movimiento

# Create your models here.
class Area(models.Model):
    nombre=models.CharField(max_length=200)
    descripcion=models.TextField()
    codigo=models.IntegerField()
    area_responsable=models.ForeignKey(Area_Responsable,on_delete=models.CASCADE,null=False,blank=False,related_name='area_responsible')
    local=models.ForeignKey(Local,on_delete=models.CASCADE,null=False,blank=False,related_name='local')
    tipo_movimiento=models.ForeignKey(Tipo_Movimiento,on_delete=models.CASCADE,null=False,blank=False,related_name='tipo_movimiento')