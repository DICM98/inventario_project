from django.db import models
from autor.models import Autor
# Create your models here.

class Libro(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Autor,on_delete=models.CASCADE,null=False,blank=False,related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)