from rest_framework import serializers
from xplorer.models import SimpleStationWeather, WeatherStation


class SimpleWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleStationWeather
        fields = "__all__"


class WeatherStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherStation
        fields = "__all__"
