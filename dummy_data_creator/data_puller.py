import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')



url = f'https://api.openweathermap.org/data/2.5/weather?lat=40&lon=-73&appid={API_KEY}'

response = requests.get(url)
print(response.json())