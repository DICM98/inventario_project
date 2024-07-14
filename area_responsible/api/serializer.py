from rest_framework import serializers
from area_responsible.models import Area_Responsible


class Area_ResponsibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area_Responsible
        fields = '__all__' 