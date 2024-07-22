from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from clasificacion.models import Clasificacion
from clasificacion.api.serializer import ClasificacionSerializer


class ClasificacionViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Clasificacion.objects.all()
    serializer_class = ClasificacionSerializer