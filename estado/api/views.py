from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from estado.models import Estado
from estado.api.serializer import EstadoSerializer


class EstadoViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer