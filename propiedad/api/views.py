from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from propiedad.models import Propiedad
from propiedad.api.serializer import PropiedadSerializer


class PropiedadViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Propiedad.objects.all()
    serializer_class = PropiedadSerializer