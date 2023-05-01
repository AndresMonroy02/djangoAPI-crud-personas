from rest_framework import serializers
from .models import Personas

class PersonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = ('id', 'nombres', 'apellidos', 'programa')
