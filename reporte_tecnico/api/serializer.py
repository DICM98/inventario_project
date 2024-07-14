from rest_framework import serializers
from reporte_tecnico.models import Reporte_Tecnico

class Reporte_TecnicoSerializer(serializers.ModelSerializer):
     class Meta:
        model = Reporte_Tecnico
        fields = '__all__' 