from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from propiedad_baja.models import Propiedad_Baja
from propiedad_baja.api.serializer import Propiedad_BajaSerializer


class Propiedad_BajaViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Propiedad_Baja.objects.all()
    serializer_class = Propiedad_BajaSerializer