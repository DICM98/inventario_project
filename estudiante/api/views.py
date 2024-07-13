from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from estudiante.models import Estudiante
from estudiante.api.serializer import EstudianteSerializer


class EstudianteViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer