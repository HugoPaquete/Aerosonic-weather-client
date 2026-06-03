#!/usr/bin/env python3
from aerosonic.weather_client import WeatherClient
import time

client = WeatherClient()

cities = ["Lisbon", "London", "Tokyo", "New York"]

for city in cities:
    client.set_city(city)
    weather = client.fetch()
    print(f"{city}: {weather.temperature:.1f}°C, wind {weather.wind_speed:.1f} km/h")
    time.sleep(0.5)
