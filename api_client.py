import requests
import os
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

def get_tirages():
    url = "https://euromillions.p.rapidapi.com/draws"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "euromillions.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()