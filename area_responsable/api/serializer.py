from rest_framework import serializers
from area_responsable.models import Area_Responsable


class Area_ResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area_Responsable
        fields = '__all__' 