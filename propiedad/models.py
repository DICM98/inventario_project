from django.db import models
from estado.models import Estado
from clasificacion.models import Clasificacion
from caracteristica.models import Caracteristica
from marca.models import Marca
from categoria.models import Categoria
from propiedad_baja.models import Propiedad_Baja


# Create your models here.
class Propiedad(models.Model):
     codigo=models.IntegerField()
     fecha_creado=models.DateTimeField(auto_now_add=True)
     nombre=models.CharField(max_length=200)
     descripcion=models.TextField()
     prestado_fecha=models.DateTimeField(auto_now_add=True)
     num_inventario=models.IntegerField()
     estado = models.ForeignKey(Estado,on_delete=models.CASCADE,null=False,blank=False,related_name='estado')
     caracteristica = models.ForeignKey(Caracteristica,on_delete=models.CASCADE,null=False,blank=False,related_name='estado')
     categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,null=False,blank=False,related_name='estado')
     marca = models.ForeignKey(Marca,on_delete=models.CASCADE,null=False,blank=False,related_name='estado')
     propiedad_baja = models.ForeignKey(Propiedad_Baja,on_delete=models.CASCADE,null=False,blank=False,related_name='estado')
     clasificacion = models.ForeignKey(Clasificacion,on_delete=models.CASCADE,null=False,blank=False,related_name='estado')
