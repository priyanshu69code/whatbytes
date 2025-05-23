# patients/serializers.py
from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'age', 'gender', 'address', 'phone', 'created_at']
        read_only_fields = ['id', 'created_at']
