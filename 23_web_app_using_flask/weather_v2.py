import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()  # take environment variables from .env.


def get_current_weather(city="London"):
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY not found in environment variables")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    try:
        response = requests.get(request_url)

        # Will raise an HTTPError for bad responses (4xx and 5xx)
        response.raise_for_status()

        weather_data = response.json()
    except requests.RequestException as e:
        return {"cod": "error", "message": str(e)}

    return weather_data


if __name__ == '__main__':
    print('\n*** Get Current Weather ***')
    city = input('\n Please enter a city name: ')

    # input validation
    if not bool(city.strip()):
        city = 'London'
    data = get_current_weather(city)
    pprint(data)

    if data.get('cod') == 200:
        print(
            f'\n--- Current Weather for {data["name"]} ---\nTemperature {data["main"]["temp"]}, feels like {data["main"]["feels_like"]}\n {data["weather"][0]["description"]}')
    else:
        print(
            f'\n--- Error: {data.get("message", "Unknown error occurred")} ---')
