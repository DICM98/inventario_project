from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from area_responsable.models import Area_Responsable
from area_responsable.api.serializer import Area_ResponsableSerializer


class Area_ResponsableViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Area_Responsable.objects.all()
    serializer_class = Area_ResponsableSerializer