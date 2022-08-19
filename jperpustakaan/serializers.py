from django.db.models import fields
from django.db.models.base import Model
from jperpustakaan.models import Kelompok
from rest_framework import serializers

class KelompokSerializers(serializers.ModelSerializer):
    class Meta:
        model = Kelompok
        fields = ['id','nama','keterangan']