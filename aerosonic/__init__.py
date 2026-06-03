# aerosonic/__init__.py
"""
AEROSONIC Weather Client
Public weather module for developers
"""

from .weather_client import WeatherClient, WeatherData, WeatherBounds

__version__ = "1.0.0"
__author__ = "Hugo Paquete"
__all__ = ["WeatherClient", "WeatherData", "WeatherBounds"]

Add __init__.py
