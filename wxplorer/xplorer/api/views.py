from rest_framework import viewsets
from xplorer.api.serializers import (
    SimpleWeatherSerializer,
    WeatherStationSerializer,
)
from xplorer.models import SimpleStationWeather, WeatherStation


class SimpleWeatherViewSet(viewsets.ModelViewSet):
    queryset = SimpleStationWeather.objects.all()
    serializer_class = SimpleWeatherSerializer


class WeatherStationViewSet(viewsets.ModelViewSet):
    queryset = WeatherStation.objects.all()
    serializer_class = WeatherStationSerializer
