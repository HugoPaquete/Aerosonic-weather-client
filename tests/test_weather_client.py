import pytest
from aerosonic.weather_client import WeatherClient

def test_client_creation():
    client = WeatherClient()
    assert client.get_current_city() == "Lisbon"

def test_set_city():
    client = WeatherClient()
    assert client.set_city("Tokyo") == True

def test_invalid_city():
    client = WeatherClient()
    assert client.set_city("Mars") == False
