from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from local.models import Local
from local.api.serializer import LocalSerializer


class LocalViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Local.objects.all()
    serializer_class = LocalSerializer