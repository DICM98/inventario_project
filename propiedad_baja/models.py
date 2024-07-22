from django.db import models
# from propiedad.models import Propiedad
# Create your models here.
class Propiedad_Baja(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    motivo= models.TextField()
    fecha=models.DateTimeField(auto_now_add=True)
    # propiedad = models.ForeignKey(Propiedad,on_delete=models.CASCADE,null=False,blank=False,related_name='propiedad')