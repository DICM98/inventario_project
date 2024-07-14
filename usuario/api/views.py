from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from usuario.models import Usuario
from usuario.api.serializer import UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer