from rest_framework import serializers
from propiedad_baja.models import Propiedad_Baja


class Propiedad_BajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propiedad_Baja
        fields = '__all__' 