from rest_framework import serializers
from caracteristica.models import Caracteristica


class CaracteristicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caracteristica
        fields = '__all__' 