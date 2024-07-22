from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from marca.models import Marca
from marca.api.serializer import MarcaSerializer


class MarcaViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer