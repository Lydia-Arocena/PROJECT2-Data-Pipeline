import requests
import numpy as np
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('waqiApiToken')

def load_csv():
    """
    Esta función sirve para cargar el csv.
    Args: No recibe parámetros.
    Return: df del csv importado.
    
    """
    return pd.read_csv("data/City_Quality_of_Life_Dataset.csv", encoding = "ISO-8859-1", index_col = 0)
    


def getquality(city):
    """
    Esta función sirve para llamar a la API tantas veces como ciudades le pase de mi columna de ciudades de mi df. Si le pasase alguna ciudad cuya info no tuviera la API, me devolvería NAN.
    Parámetros: city(string)
    Return: el valor de la calidad del tiempo que es una de los datos que tiene esta API.

    """
    try:
        url =f"https://api.waqi.info/feed/{city}/?token={API_TOKEN}"
        response = requests.get(url).json()
        return response["data"]["aqi"]
    except:
        return np.nan


def quality_level (x):
    """
    Esta función hace una clasificación de la calidad del aire en función del parámetro que recibe de la API.
    Parámetros: calidad del aire (string)
    Return: Categoría de la calidad del aire.

    """
    try:
        x = int(x)
        if x<=50:
            return "Good"
        elif 51<=x<=100:
            return "Moderate"
        elif 101<=x<=150:
            return "Unhealthy for Sensitive Groups"
        elif 151<=x<=200:
            return "Unhealthy"
        elif 201<=x<=300:
            return "Very Unhealthy"
        else:
            return "Hazardous"
    except:
        return np.nan
