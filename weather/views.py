import os
import requests

from .forms import CityForm
from django.contrib import messages
from django.shortcuts import render


def home(request):

    if request.method == 'POST':
        appid = os.environ.get('API_KEY')
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['name']
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={appid}'
            response = requests.get(url).json()

            if response['cod'] == 200:
                city_weather = {
                    'city': city,
                    'temp': response['main']['temp'],
                    'desc': response['weather'][0]['description']
                }

                args = {
                    'city_weather': city_weather,
                }

                return render(request, 'weather/city.html', args)
            else:
                messages.warning(request, 'Invalid City Name.')
    else:
        form = CityForm()

    args = {
        'form': form
    }

    return render(request, 'weather/home.html', args)
