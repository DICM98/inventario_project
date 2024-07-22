from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from caracteristica.models import Caracteristica
from caracteristica.api.serializer import CaracteristicaSerializer


class CaracteristicaViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Caracteristica.objects.all()
    serializer_class = CaracteristicaSerializer