from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from area.models import Area
from area.api.serializer import AreaSerializer


class AreaViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Area.objects.all()
    serializer_class = AreaSerializer