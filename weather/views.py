import os
import requests
from django.shortcuts import render


def home(request):
    appid = os.environ.get('API_KEY')
    city = 'Cairo' # Test City
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={appid}'
    r = requests.get(url).json()

    city_weather = {
        'city': city,
        'temp': r['main']['temp'],
        'desc': r['weather'][0]['description']
    }

    args = {
        'city_weather': city_weather
    }

    return render(request, 'weather/city.html', args)
