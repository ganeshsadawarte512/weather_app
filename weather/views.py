from rest_framework import generics
from .models import WeatherData
from .serializers import WeatherDataSerializer
from django_filters.rest_framework import DjangoFilterBackend

class WeatherDataList(generics.ListAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'date': ['year'],        # Filter by year
        'region': ['exact'],     # Filter by region
        'parameter': ['exact'],  # Filter by parameter
    }
from django.shortcuts import render
from .models import WeatherData
def weather_data_view(request):
    years = WeatherData.objects.dates('date', 'year', order='DESC')
    regions = WeatherData.objects.values_list('region', flat=True).distinct()
    parameters = WeatherData.objects.values_list('parameter', flat=True).distinct()

    return render(request, 'weather_data.html', {
        'years': [y.year for y in years],
        'regions': regions,
        'parameters': parameters
    })


from rest_framework import generics
from .models import WeatherData
from .serializers import WeatherDataSerializer
from django_filters.rest_framework import DjangoFilterBackend

class WeatherDataList(generics.ListAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'date': ['year'],        # Filter by year
        'region': ['exact'],     # Filter by region
        'parameter': ['exact'],  # Filter by parameter
    }
