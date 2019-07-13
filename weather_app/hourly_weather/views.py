from django.shortcuts import render
from weather.models import City
import requests

# Create your views here.
def hourly_view(request, *args, **kwargs):

    url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&APPID=211d1a9601c8fad4482f702ee116b1f3'


    cities = City.objects.all()
    r = requests.get(url.format(cities[0])).json()
    hourly_updates = []
    for hour in r['list']:
        date_time = hour['dt_txt'].split(" ")
        time = date_time[1]
        if int(time[:2]) < 12:
            time += " AM"
        else:
            time += " PM"
        each_hour = {
        'date': date_time[0],
        'time': time,
        'temperature': hour['main']['temp'],
        'icon': hour['weather'][0]['icon'],
        'description': hour['weather'][0]['description']
        }
        hourly_updates.append(each_hour)
    return render(request, "hourly.html", {'hourly_data': hourly_updates})
