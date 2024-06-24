import requests
from dotenv import load_dotenv
import os
from pprint import pprint


load_dotenv()  # take environment variables from .env.


def get_current_weather():
    print('\n*** Get Current Weather ***')

    city = input('\n Please enter a city name: ')

    request_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_KEY")}&units=metric'

    print(f'request_url = {request_url}')

    weather_data = requests.get(request_url).json()
    pprint(weather_data)

    print(
        f'\n--- Current Weather for {weather_data["name"]} ---\nTemperature {weather_data["main"]["temp"]}, feels like {weather_data["main"]["feels_like"]}\n {weather_data["weather"][0]["description"]}')


if __name__ == '__main__':
    get_current_weather()
