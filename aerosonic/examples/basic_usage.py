#!/usr/bin/env python3
from aerosonic.weather_client import WeatherClient

client = WeatherClient()
weather = client.fetch()

print(f"City: {weather.city}")
print(f"Temperature: {weather.temperature:.1f}°C")
print(f"Wind: {weather.wind_speed:.1f} km/h")
