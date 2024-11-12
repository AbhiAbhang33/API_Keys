import requests
from django.conf import settings

def get_data_from_rapidapi(endpoint, params=None):
    url = f"https://livescore6.p.rapidapi.com/v2/search"
    headers = {
        "X-RapidAPI-Key": settings.RAPIDAPI_KEY,
        "X-RapidAPI-Host": "livescore6.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()
