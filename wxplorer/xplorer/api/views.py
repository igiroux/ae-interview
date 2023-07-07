from rest_framework import viewsets

from xplorer.api.serializers import SimpleWeatherSerializer, WeatherStationSerializer
from xplorer.models import SimpleWeather, WeatherStation


class SimpleWeatherViewSet(viewsets.ModelViewSet):
    queryset = SimpleWeather.objects.all()
    serializer_class = SimpleWeatherSerializer


class WeatherStationViewSet(viewsets.ModelViewSet):
    queryset = WeatherStation.objects.all()
    serializer_class = WeatherStationSerializer