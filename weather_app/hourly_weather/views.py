from django.shortcuts import render
from weather.models import City
import requests

# Create your views here.
def hourly_view(request, *args, **kwargs):

    url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&APPID=211d1a9601c8fad4482f702ee116b1f3'


    cities = City.objects.all()
    print(cities)

    # for new_city in cities:
    #     r = requests.get(url.format(new_city)).json()
    #     print(r['list'][0]['dt_txt'])
    r = requests.get(url.format(cities[0])).json()
    hourly_updates = []
    for hour in r['list']:
        date_time = hour['dt_txt'].split(" ")
        each_hour = {
        'date': date_time[0],
        'time': date_time[1],
        'temperature': hour['main']['temp'],
        'icon': hour['weather'][0]['icon']
        }
        hourly_updates.append(each_hour)
    print(hourly_updates)
        # print(hour['dt_txt'])
        # print(hour['main']['temp'])
    return render(request, "hourly.html", {'hourly_data': hourly_updates})
