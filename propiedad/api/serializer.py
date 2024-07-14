from rest_framework import serializers
from propiedad.models import Propiedad


class PropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propiedad
        fields = '__all__' 