"""graph_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from API import views
from django.conf.urls import url 

#router = routers.DefaultRouter()
#router.register(r'city', views.CityViewSet,'city')
#router.register(r'year', views.YearViewSet,'year')
#router.register(r'AverageTemperatureByCity',views.AverageTemperatureByCityViewSet,'AverageTemperatureByCity')
#router.register(r'AverageTemperatureByYear',views.AverageTemperatureByYearViewSet,'AverageTemperatureByYear')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^city/$',views.CityView),
    path('AverageTemperatureByYear/',views.AverageTemperatureByYear),
    path('year/',views.YearView),
    path('AverageTemperatureByCity/',views.AverageTemperatureByCity),
    #path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
