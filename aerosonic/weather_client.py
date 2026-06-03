#!/usr/bin/env python3
"""
Weather Client - Public Module
Simple, clean weather data client for Python developers.
"""

import time
import math
import random
from datetime import datetime
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False


class WeatherBounds:
    """Normalization bounds for weather data"""
    TEMP_MIN, TEMP_MAX = -30.0, 50.0
    WIND_MIN, WIND_MAX = 0.0, 50.0
    PRECIP_MIN, PRECIP_MAX = 0.0, 100.0
    
    @classmethod
    def normalize(cls, value: float, min_val: float, max_val: float) -> float:
        if max_val <= min_val:
            return 0.5
        return max(0.0, min(1.0, (value - min_val) / (max_val - min_val)))


@dataclass
class WeatherData:
    """Weather data structure"""
    temperature: float = 15.0
    wind_speed: float = 10.0
    precipitation: float = 0.0
    city: str = "Lisbon"
    timestamp: float = field(default_factory=time.time)
    temp_norm: float = 0.5
    wind_norm: float = 0.25
    precip_norm: float = 0.0
    source: str = "Open-Meteo"
    
    def to_dict(self) -> Dict:
        return {
            'temperature': self.temperature,
            'wind_speed': self.wind_speed,
            'precipitation': self.precipitation,
            'city': self.city,
            'timestamp': self.timestamp,
            'source': self.source
        }
    
    def __repr__(self) -> str:
        return (f"WeatherData(temp={self.temperature:.1f}°C, "
                f"wind={self.wind_speed:.1f}km/h, "
                f"rain={self.precipitation:.1f}mm, "
                f"city={self.city})")


PUBLIC_CITIES: Dict[str, Tuple[float, float]] = {
    'Lisbon': (38.7223, -9.1393),
    'Porto': (41.1579, -8.6291),
    'London': (51.5074, -0.1278),
    'Paris': (48.8566, 2.3522),
    'Berlin': (52.5200, 13.4050),
    'Rome': (41.9028, 12.4964),
    'Madrid': (40.4168, -3.7038),
    'New York': (40.7128, -74.0060),
    'Tokyo': (35.6762, 139.6503),
    'Sydney': (-33.8688, 151.2093),
    'Sao Paulo': (-23.5505, -46.6333),
    'Cape Town': (-33.9249, 18.4241),
}


class WeatherClient:
    """Simple weather data client for developers"""
    
    def __init__(self, debug: bool = False):
        self.city = "Lisbon"
        self._lat, self._lon = PUBLIC_CITIES["Lisbon"]
        self.debug = debug
        self._cache = None
        self._last_fetch = 0
        self._manual_mode = False
        self._manual_values = {'temperature': 20, 'wind_speed': 10, 'precipitation': 0}
    
    def set_city(self, city: str) -> bool:
        if city in PUBLIC_CITIES:
            self.city = city
            self._lat, self._lon = PUBLIC_CITIES[city]
            self._cache = None
            return True
        return False
    
    def get_cities(self) -> List[str]:
        return list(PUBLIC_CITIES.keys())
    
    def get_current_city(self) -> str:
        return self.city
    
    def fetch(self) -> WeatherData:
        if self._manual_mode:
            return self._manual_weather()
        
        now = time.time()
        if self._cache and (now - self._last_fetch) < 5:
            return self._cache
        
        if REQUESTS_AVAILABLE:
            data = self._fetch_api()
        else:
            data = None
        
        if data is None:
            data = self._fallback_weather()
        
        self._cache = data
        self._last_fetch = now
        return data
    
    def _fetch_api(self) -> Optional[WeatherData]:
        try:
            resp = requests.get(
                "https://api.open-meteo.com/v1/forecast",
                params={
                    "latitude": self._lat,
                    "longitude": self._lon,
                    "current_weather": "true"
                },
                timeout=10
            )
            
            if resp.status_code != 200:
                return None
            
            data = resp.json()
            current = data.get("current_weather", {})
            
            result = WeatherData(
                temperature=current.get("temperature", 15.0),
                wind_speed=current.get("windspeed", 10.0),
                city=self.city,
                source="Open-Meteo"
            )
            
            result.temp_norm = WeatherBounds.normalize(result.temperature,
                                                       WeatherBounds.TEMP_MIN,
                                                       WeatherBounds.TEMP_MAX)
            result.wind_norm = WeatherBounds.normalize(result.wind_speed,
                                                        WeatherBounds.WIND_MIN,
                                                        WeatherBounds.WIND_MAX)
            return result
            
        except Exception as e:
            if self.debug:
                print(f"[WeatherClient] API error: {e}")
            return None
    
    def _manual_weather(self) -> WeatherData:
        result = WeatherData(
            temperature=self._manual_values.get('temperature', 20),
            wind_speed=self._manual_values.get('wind_speed', 10),
            precipitation=self._manual_values.get('precipitation', 0),
            city=self.city,
            source="Manual"
        )
        result.temp_norm = WeatherBounds.normalize(result.temperature,
                                                   WeatherBounds.TEMP_MIN,
                                                   WeatherBounds.TEMP_MAX)
        result.wind_norm = WeatherBounds.normalize(result.wind_speed,
                                                    WeatherBounds.WIND_MIN,
                                                    WeatherBounds.WIND_MAX)
        return result
    
    def _fallback_weather(self) -> WeatherData:
        hour = datetime.now().hour
        temp_base = 18 + 2 * math.sin((hour - 14) * math.pi / 12)
        
        result = WeatherData(
            temperature=temp_base + random.uniform(-2, 2),
            wind_speed=10 + random.uniform(-5, 10),
            precipitation=max(0, random.uniform(0, 5)),
            city=self.city,
            source="Fallback"
        )
        
        result.temp_norm = WeatherBounds.normalize(result.temperature,
                                                   WeatherBounds.TEMP_MIN,
                                                   WeatherBounds.TEMP_MAX)
        result.wind_norm = WeatherBounds.normalize(result.wind_speed,
                                                    WeatherBounds.WIND_MIN,
                                                    WeatherBounds.WIND_MAX)
        return result


def create_weather_client(debug: bool = False) -> WeatherClient:
    return WeatherClient(debug=debug)


if __name__ == "__main__":
    client = WeatherClient(debug=True)
    weather = client.fetch()
    print(f"\n{weather}")
