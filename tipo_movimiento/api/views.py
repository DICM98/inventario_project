from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from tipo_movimiento.models import Tipo_Movimiento
from tipo_movimiento.api.serializer import Tipo_MovimientoSerializer


class Tipo_MovimientoViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Tipo_Movimiento.objects.all()
    serializer_class = Tipo_MovimientoSerializer