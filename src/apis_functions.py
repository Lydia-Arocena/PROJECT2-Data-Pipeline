import requests
import numpy as np
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('waqiApiToken')

def load_csv():
    return pd.read_csv("data/City_Quality_of_Life_Dataset.csv", encoding = "ISO-8859-1", index_col = 0)
    


def getquality(city):
    try:
        url =f"https://api.waqi.info/feed/{city}/?token={API_TOKEN}"
        response = requests.get(url).json()
        return response["data"]["aqi"]
    except:
        return np.nan

def quality_level (x):
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
