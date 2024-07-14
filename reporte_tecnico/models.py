from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Reporte_Tecnico (models.Model):
    transfer_request=models.TextField()
    authorized=models.BooleanField()
    position=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    authorized_date=models.DateTimeField(auto_now_add=True)
    approved=models.BooleanField()
    approved_date=models.DateTimeField(auto_now_add=True)
    transported_date=models.DateTimeField(auto_now_add=True)
    name_fact=models.CharField(max_length=200)
    