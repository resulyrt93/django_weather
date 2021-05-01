import json

from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings

import requests


class WeatherData(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def prepare_api_query_params(request):
        _data = request.data

        forecast_day = _data.get('forecast_day')
        city = _data.get('city')

        if city is None or forecast_day is None:
            raise APIException('city and forecast_day fields are required')

        if not isinstance(forecast_day, int) or forecast_day > 5:
            raise APIException('Forecast day should be equal or less than 5')

        params = {
            'format': 'json',
            'num_of_days': forecast_day,
            'q': city,
            'key': settings.WORLD_WEATHER_ONLINE_API_KEY
        }

        return params

    def post(self, request):

        url = settings.WORLD_WEATHER_ONLINE_API_URL
        query_params = self.prepare_api_query_params(request)

        request_response = requests.get(url, params=query_params)

        if request_response.status_code == 200:
            data = json.loads(request_response.text)
            return Response(data, status=status.HTTP_200_OK)
        else:
            raise APIException('Could not be accessed to API')