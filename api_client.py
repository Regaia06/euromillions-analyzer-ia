import os
import requests

def get_tirages():
    url = "https://euromillions.p.rapidapi.com/draws"
    headers = {
        "X-RapidAPI-Key": os.environ.get("RAPIDAPI_KEY"),
        "X-RapidAPI-Host": "euromillions.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
