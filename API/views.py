from django.shortcuts import render 
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser 
from rest_framework import status
from .models import *
from rest_framework import viewsets
from API.serializers import *
from django.db.models import Avg


'''class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer'''


@csrf_exempt
def CityView(request):
    if request.method == 'GET':
        queryset = City.objects.all()
        City_Serializer = CitySerializer(queryset, many=True)
        return JsonResponse(City_Serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'


'''class YearViewSet(viewsets.ModelViewSet):
    queryset = Temperature.objects.values('Year').distinct()
    serializer_class = TemperatureSerializer'''

@csrf_exempt
def YearView(request):
    if request.method == 'GET':
        queryset = Temperature.objects.values('Year').distinct()
        Year_Serializer =  TemperatureSerializer(queryset, many=True)
        return JsonResponse(Year_Serializer.data, safe=False)

'''class AverageTemperatureByYearViewSet(viewsets.ModelViewSet):
    queryset = Temperature.objects.values('Year').annotate(Avg('temperature'))
    serializer_class = AverageTemperatureSerializer'''

@csrf_exempt
def AverageTemperatureByYear(request):
    if request.method == 'GET':
        queryset = Temperature.objects.values('Year').annotate(Avg('temperature'))
        Temp_Serializer = AverageTemperatureSerializer(queryset, many=True)
        return JsonResponse(Temp_Serializer.data, safe=False)
    elif request.method == 'POST':
        Temp_data = JSONParser().parse(request)
        queryset = Temperature.objects.values('Year').annotate(Avg('temperature')).filter(Year=Temp_data['Year'])
        Temp_Serializer = AverageTemperatureSerializer(queryset, many=True)
        return JsonResponse(Temp_Serializer.data, safe=False)
    

'''class AverageTemperatureByCityViewSet(viewsets.ModelViewSet):
    queryset = Temperature.objects.values('ID').annotate(Avg('temperature'))
    serializer_class = AverageTemperatureByCitySerializer'''

@csrf_exempt
def AverageTemperatureByCity(request):
    if request.method == 'GET':
        queryset = Temperature.objects.values('ID').annotate(Avg('temperature'))
        City_Serializer =  AverageTemperatureByCitySerializer(queryset, many=True)
        return JsonResponse(City_Serializer.data, safe=False)
    elif request.method == 'POST':
        Temp_data = JSONParser().parse(request)
        if(int(Temp_data['Year'])==0):
            queryset = Temperature.objects.values('ID').annotate(Avg('temperature')).filter(ID=Temp_data['City_Name'])
        else:
            queryset = Temperature.objects.filter(ID = Temp_data['City_Name'],Year = Temp_data['Year']).values('ID').annotate(Avg('temperature'))
        Temp_Serializer =  AverageTemperatureByCitySerializer(queryset, many=True)
        return JsonResponse(Temp_Serializer.data, safe=False)
    