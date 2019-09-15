from django.shortcuts import render
from weather.models import City
import requests
import time

# Create your views here.
def hourly_view(request, *args, **kwargs):

    url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&APPID=211d1a9601c8fad4482f702ee116b1f3'

    print(kwargs)
    cities = City.objects.all()
    r = requests.get(url.format(kwargs['city'])).json()
    hourly_updates = []

    for hour in r['list']:
        date_time = hour['dt_txt'].split(" ")
        print(date_time)
        time = date_time[1]

        each_hour = {
        'date': date_time[0],
        'time': time,
        'temperature': hour['main']['temp'],
        'icon': hour['weather'][0]['icon'],
        'description': hour['weather'][0]['description']
        }
        hourly_updates.append(each_hour)
    return render(request, "hourly.html", {'city': kwargs['city'],'hourly_data': hourly_updates})
