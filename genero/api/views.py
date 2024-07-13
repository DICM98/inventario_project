from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from genero.models import Genero
from genero.api.serializer import GeneroSerializer


class GeneroViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer