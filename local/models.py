from django.db import models
from propiedad.models import Propiedad

# Create your models here.
class Local(models.Model):
    name=models.CharField(max_length=200)
    code=models.IntegerField()
    description=models.TextField()
    responsible=models.TextField()
    propiedad = models.ForeignKey(Propiedad,on_delete=models.CASCADE,null=False,blank=False,related_name='propiedad')