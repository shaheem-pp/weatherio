import json
import urllib.request
from django.shortcuts import redirect, render


# Create your views here.
import weatherio.secrets


def index(request):
    if request.method == 'POST':
        city = (request.POST['city']).capitalize()
        searched = 1
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city +
            '&appid=' + weatherio.secrets.API_KEY + '&units=metric').read()
        list_of_data = json.loads(source)
        data = {
            'city': city,
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
                          + str(list_of_data['coord']['lat']),
            "temp": int(list_of_data['main']['temp']),
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "logo": int(list_of_data['weather'][0]['id']),
            "searched": searched
        }
    else:
        data = {"searched": 0}
    return render(request, "index.html", data)
