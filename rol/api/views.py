from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rol.models import Rol
from rol.api.serializer import RolSerializer


class RolViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Rol.objects.all()
    serializer_class = RolSerializer