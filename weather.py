import requests
import secrets

def get_weather_forecast():
    # request weather json package using OpenWeatherMap api
    app_id = secrets.APP_ID
    city = input('What city do you want to look up? ')
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=imperial&APPID=' + app_id
    weather_request = requests.get(url)
    weather_json = weather_request.json()

    # get weather description, min and mex temps
    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']

    # write the forecast message with our variables loading.
    forecast = 'The forecast for today in '+ city + ' is '
    forecast += description + ' with a high of ' + str(int(temp_max))
    forecast += ' and a low of ' + str(int(temp_min))

    return forecast