from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from autor.models import Autor
from autor.api.serializer import AutorSerializer


class AutorViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer