from django.contrib import admin
from .models import City, Temperature

@admin.register(City)
class CityAdmin(admin.ModelAdmin):

    list_display = ('id', 'City_Name')
    fields = ('City_Name',)

@admin.register(Temperature)
class TemperatureAdmin(admin.ModelAdmin):

    list_display = ('ID', 'Year', 'temperature')
    fields = ('ID', 'Year', 'temperature',)
