from django.db import models
from django.db.models import SET_NULL
from categoria.models import Categoria

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    description = models.TextField()
    price = models.BigIntegerField()
    published = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete= SET_NULL, null=True)