import requests
from typing import Dict
from config_data.config import API_KEY


def weather_request(city: str) -> Dict:
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

    querystring = {"q": city, "days": "3"}

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())
    return response.json()
