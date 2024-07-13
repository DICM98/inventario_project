from django.db import models
from libro.models import Libro
# Create your models here.

class Genero(models.Model):
    title = models.CharField(max_length=50)
    books = models.ManyToManyField(Libro, related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
