from rest_framework import serializers
from .models import *

class ReporterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','mobile_number']


class IncidentSerializer(serializers.ModelSerializer):
    # reporter    =    ReporterSerializer()
    class Meta:
        model=Incident
        fields='__all__'
        read_only_fields = ['incidentId','created_at']

