from rest_framework import serializers
from tipo_movimiento.models import Tipo_Movimiento

class Tipo_MovimientoSerializer(serializers.ModelSerializer):
     class Meta:
        model = Tipo_Movimiento
        fields = '__all__' 