from .models import *
from rest_framework import serializers


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'City_Name']


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ['Year']

class AverageTemperatureSerializer(serializers.ModelSerializer):
    temperature__avg = serializers.DecimalField(max_digits=5, decimal_places=2)
    class Meta:
        model = Temperature
        fields = ['Year','temperature__avg']

class AverageTemperatureByCitySerializer(serializers.Serializer):
    temperature__avg = serializers.DecimalField(max_digits=5, decimal_places=2)
    ID = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = Temperature
        fields = ['ID', 'temperature__avg']