from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class SimpleStationWeather(models.Model):
    forecast_time = models.DateTimeField()
    temperature = models.FloatField()
    humidity = models.PositiveIntegerField()
    cloudiness = models.PositiveIntegerField()
    station = models.ForeignKey("WeatherStation", on_delete=models.CASCADE)

    class Meta:
        unique_together = (("forecast_time", "station"),)


class WeatherStation(models.Model):
    station_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    longitude = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)]
    )
    latitude = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)]
    )
    altitude = models.PositiveIntegerField()
