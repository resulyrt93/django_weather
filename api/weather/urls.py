from django.urls import path
from .views import WeatherData

urlpatterns = [
    path('weather-data/', WeatherData.as_view(), name='weather_data'),
]