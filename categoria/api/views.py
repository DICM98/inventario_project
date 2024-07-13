from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from categoria.models import Categoria
from categoria.api.serializer import CategoriaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer