from django.db import models

# Create your models here.
class Reporte_Tecnico (models.Model):
    solicitud_transferencia=models.TextField()
    autorizado=models.BooleanField()
    posicion=models.CharField(max_length=100)
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    fecha_autorizado=models.DateTimeField(auto_now_add=True)
    aprobado=models.BooleanField()
    fecha_aprobado=models.DateTimeField(auto_now_add=True)
    fecha_traspaso=models.DateTimeField(auto_now_add=True)
    nombre_hecho=models.CharField(max_length=200)
    valor=models.IntegerField()
    