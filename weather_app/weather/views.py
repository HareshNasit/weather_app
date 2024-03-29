from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm
# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=de144db93b695a9bfe6425d504b7a595'
    cities = City.objects.all()
    err_msg = ''
    message = ''
    message_class = ''
    ip_info = requests.get('https://ipinfo.io/')
    information = ip_info.json()
    print(information['city'])
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()
            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()
                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = "City does not exist in the world"
            else:
                err_msg = 'City already exists in the database'
        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'City added successfully!'
            message_class = 'is-success'
    print(err_msg)
    form = CityForm()
    weather_data = []

    for city in cities:
        print(city)
        r = requests.get(url.format(city)).json()
        print(r)
        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'humidity': r['main']['humidity'],
        }
        weather_data.append(city_weather)
    # print(weather_data)
    context  = {
        'weather_data': weather_data,
        'form': form,
        'message': message,
        'message_class': message_class
    }
    return render(request, 'weather/weather.html', context)

def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()
    return redirect('home')
