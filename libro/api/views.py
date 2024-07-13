from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from libro.models import Libro
from libro.api.serializer import LibroSerializer


class LibroViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer