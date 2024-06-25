import requests
import os
from dotenv import load_dotenv
from pprint import pprint


load_dotenv()  # take environment variables from .env.


def get_current_weather(city="London"):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_KEY")}&units=metric'
    weather_data = requests.get(request_url).json()
    return weather_data


if __name__ == '__main__':

    print('\n*** Get Current Weather ***')
    city = input('\n Please enter a city name: ')
    weather_data = get_current_weather(city)
    pprint(weather_data)
    print(
        f'\n--- Current Weather for {weather_data["name"]} ---\nTemperature {weather_data["main"]["temp"]}, feels like {weather_data["main"]["feels_like"]}\n {weather_data["weather"][0]["description"]}')
