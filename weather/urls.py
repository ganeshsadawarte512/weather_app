from django.urls import path
from .views import weather_data_view, WeatherDataList

urlpatterns = [
    path('api/weather/data/', WeatherDataList.as_view(), name='weather-data-api'),
    path('weather/', weather_data_view, name='weather-data-view'),
]
from django.urls import path
from .views import WeatherDataList

urlpatterns = [
    path('data/', WeatherDataList.as_view(), name='weather-data-api'),
]
