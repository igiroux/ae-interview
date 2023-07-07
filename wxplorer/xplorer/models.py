from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# YAGNI
# country_alpha3 = models.CharField(max_length=3, default="FRA")
# class Meta:
#     constraints = models.UniqueConstraint(
#         fields=['station_id', 'country_alpha3'],
#         name="unique_isoalpha3_station_id",
#     )


class SimpleWeather(models.Model):
    forecast_time = models.DateTimeField()
    temperature = models.PositiveIntegerField()
    humidity = models.PositiveIntegerField()
    cloudiness = models.PositiveIntegerField()


class WeatherStation(models.Model):
    station_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    longitude = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)])
    latitude = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)])
    altitude = models.PositiveIntegerField()
    weather_history = models.ForeignKey(SimpleWeather, on_delete=models.CASCADE)
