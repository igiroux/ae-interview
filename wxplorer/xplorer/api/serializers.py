from rest_framework import serializers

from xplorer.models import SimpleWeather, WeatherStation


class SimpleWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleWeather
        fields = '__all__'

class WeatherStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherStation
        fields = '__all__'