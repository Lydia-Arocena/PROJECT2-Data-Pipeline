import requests

import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('waqiApiToken')

def getCities():
    return ["madrid", "london", "malaga"]

def onGetCityWheather(cityWheatherResponse):
    print(cityWheatherResponse.json())

def getCityWheatherURL(city):
    return f'https://api.waqi.info/feed/{city}/?token={API_TOKEN}'

def getCityWheather(city):
    return requests.get(getCityWheatherURL(city))

def watchCitiesWeather(cities):
    for city in cities:
        weather = getCityWheather(city)
        onGetCityWheather(weather)
    

watchCitiesWeather(getCities())
    

