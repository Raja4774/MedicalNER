from django.db.models import fields
from rest_framework import serializers

from search.models import MedicineModel


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineModel
        fields = '__all__'
