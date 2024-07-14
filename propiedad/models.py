from django.db import models

# Create your models here.
class Propiedad(models.Model):
     code=models.IntegerField()
     category=models.CharField()
     created_at=models.DateTimeField(auto_now_add=True)
     classification=models.CharField(max_length=100)
     characteristic=models.CharField(max_length=100)
     name=models.CharField(max_length=200)
     status=models.TextField()
     description=models.TextField()
     brand=models.CharField(max_length=100)
     bowered =models.CharField(max_length=100)
     inventory_number=models.IntegerField()
     range=models.TextField()