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
    y = serializers.DecimalField(max_digits=5, decimal_places=2)
    name = serializers.CharField()
    class Meta:
        model = Temperature
        fields = ['name','y']

class AverageTemperatureByCitySerializer(serializers.Serializer):
    y = serializers.DecimalField(max_digits=5, decimal_places=2)
    name = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = Temperature
        fields = ['name', 'y']