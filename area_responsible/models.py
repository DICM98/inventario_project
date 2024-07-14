from django.db import models
from usuario.models import Usuario

# Create your models here.
class Area_Responsible(models.Model):
     name_responsible=models.CharField(max_length=200)
     output_responsible=models.CharField(max_length=200)
     entry_responsible=models.CharField(max_length=200)
     created_at=models.DateTimeField(auto_now_add=True)
     usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE,null=False,blank=False,related_name='usuario')