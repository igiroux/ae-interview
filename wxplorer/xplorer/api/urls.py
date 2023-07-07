from django.urls import include, path
from rest_framework import routers
from xplorer.api.views import SimpleWeatherViewSet, WeatherStationViewSet


router = routers.DefaultRouter()
router.register(r'weather', SimpleWeatherViewSet)
router.register(r'stations', WeatherStationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]