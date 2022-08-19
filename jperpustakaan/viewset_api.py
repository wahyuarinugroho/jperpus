from rest_framework.decorators import permission_classes
from jperpustakaan.models import Kelompok
from jperpustakaan.serializers import KelompokSerializers
from rest_framework import viewsets, permissions

class KelompokViewset(viewsets.ModelViewSet):
    queryset = Kelompok.objects.all()
    serializer_class = KelompokSerializers
    permission_classes = [permissions.IsAuthenticated]