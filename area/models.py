from django.db import models
from area_responsible.models import Area_Responsible
from local.models import Local
from tipo_movimiento.models import  Tipo_Movimiento

# Create your models here.
class Area(models.Model):
    name_area=models.CharField(max_length=200)
    description=models.TextField()
    code=models.IntegerField()
    responsible=models.TextField()
    area_responsible=models.ForeignKey(Area_Responsible,on_delete=models.CASCADE,null=False,blank=False,related_name='area_responsible')
    local=models.ForeignKey(Local,on_delete=models.CASCADE,null=False,blank=False,related_name='local')
    tipo_movimiento=models.ForeignKey(Tipo_Movimiento,on_delete=models.CASCADE,null=False,blank=False,related_name='tipo_movimiento')