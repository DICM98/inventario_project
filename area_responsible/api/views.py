from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from area_responsible.models import Area_Responsible
from area_responsible.api.serializer import Area_ResponsibleSerializer


class Area_ResponsibleViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Area_Responsible.objects.all()
    serializer_class = Area_ResponsibleSerializer