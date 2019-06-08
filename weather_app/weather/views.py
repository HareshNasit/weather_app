from django.shortcuts import render
import requests
# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=de144db93b695a9bfe6425d504b7a595'
    city = 'Doha'
    r = requests.get(url.format(city)).json()
    #print(r)

    city_weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon']
    }
    print(city_weather)

    context  = {'city_weather': city_weather}
    return render(request, 'weather/weather.html', context)
