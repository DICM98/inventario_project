from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from reporte_tecnico.models import Reporte_Tecnico
from reporte_tecnico.api.serializer import Reporte_TecnicoSerializer


class Reporte_TecnicoViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Reporte_Tecnico.objects.all()
    serializer_class = Reporte_TecnicoSerializer