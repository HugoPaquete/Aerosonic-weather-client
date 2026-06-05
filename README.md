# AEROSONIC Weather Client

> Free and open-source Python weather client. Fetches real-time meteorological data from Open-Meteo API with procedural fallback and automatic normalization.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Requests](https://img.shields.io/badge/requests-2.28+-green.svg)](https://requests.readthedocs.io/)
[![FCT](https://img.shields.io/badge/FCT-2024.09158.CEECIND-blue.svg)](https://www.fct.pt)
[![INET-md](https://img.shields.io/badge/INET-md-University%20of%20Aveiro-purple.svg)](https://www.inetmd.pt)
[![DeepSeek](https://img.shields.io/badge/DeepSeek-AI%20Assisted-orange.svg)](https://deepseek.com)
[![Website](https://img.shields.io/badge/website-hugopaquete.com-1e3a8a.svg)](https://www.hugopaquete.com)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20538818.svg)](https://doi.org/10.5281/zenodo.20538817)


---

## Table of Contents

- [Quick Start](#quick-start)
- [Change City](#change-city)
- [Available Cities](#available-cities)
- [Normalization (0-1 range)](#normalization-0-1-range)
- [Normalization Bounds](#normalization-bounds)
- [Manual Mode (Testing)](#manual-mode-testing)
- [Data Structure](#data-structure)
- [API Reference](#api-reference)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [Development](#development)
- [Funding](#funding)
- [Credits](#credits)
- [Citation](#citation)
- [License](#license)
- [Contact](#contact)
- [Links](#links)
- [Installation](#installation)

---

## Quick Start

```python
from aerosonic.weather_client import WeatherClient

client = WeatherClient()
weather = client.fetch()

print(f"{weather.city}: {weather.temperature}°C, wind {weather.wind_speed} km/h")

Change City

python
client.set_city("Tokyo")
weather = client.fetch()
print(f"Tokyo: {weather.temperature}°C")

Available Cities

Continent	Cities
Europe	Lisbon, Porto, London, Paris, Berlin, Rome, Madrid
North America	New York
Asia	Tokyo
Oceania	Sydney
South America	Sao Paulo
Africa	Cape Town

Normalization (0-1 range)

python
weather = client.fetch()

print(f"Temperature: {weather.temp_norm:.2f}")
print(f"Wind speed: {weather.wind_norm:.2f}")

Normalization Bounds

Parameter	Min	Max	Formula
Temperature	-30°C	50°C	(value + 30) / 80
Wind speed	0 km/h	50 km/h	value / 50
Precipitation	0 mm	100 mm	value / 100

Manual Mode (Testing)

python
client.set_manual_mode(True, {
    "temperature": 30,
    "wind_speed": 25,
    "precipitation": 10
})

weather = client.fetch()
print(f"Manual mode: {weather.temperature}°C")

client.set_manual_mode(False)

Data Structure

python
@dataclass
class WeatherData:
    temperature: float      # °C (-30 to 50)
    wind_speed: float       # km/h (0 to 50)
    precipitation: float    # mm (0 to 100)
    city: str               # City name
    temp_norm: float        # 0-1 normalized
    wind_norm: float        # 0-1 normalized
    source: str             # Data source ('api' or 'procedural')
    timestamp: float        # Unix timestamp

API Reference

WeatherClient Methods
Method	Returns	Description
fetch()	WeatherData	Get current weather data
set_city(city)	bool	Change current city
get_cities()	List[str]	List all available cities
get_current_city()	str	Get current city name
set_manual_mode(enabled, data)	None	Enable/disable manual mode

WeatherData Attributes

Attribute	Type	Range	Description
temperature	float	-30 to 50	Temperature in °C
wind_speed	float	0 to 50	Wind speed in km/h
precipitation	float	0 to 100	Precipitation in mm
city	str	-	City name
temp_norm	float	0 to 1	Normalized temperature
wind_norm	float	0 to 1	Normalized wind speed
source	str	-	Data source ('api' or 'procedural')
timestamp	float	-	Unix timestamp

Testing

bash
pip install pytest
pytest tests/ -v

Project Structure

text
Aerosonic-weather-client/
├── aerosonic/
│   ├── __init__.py
│   └── weather_client.py
├── examples/
│   ├── basic_usage.py
│   └── advanced_usage.py
├── tests/
│   └── test_weather_client.py
├── README.md
├── LICENSE
└── requirements.txt

Development

bash
git clone https://github.com/HugoPaquete/Aerosonic-weather-client.git
cd Aerosonic-weather-client
pip install -e . pytest black
pytest tests/
black aerosonic/ tests/

Funding

This project is part of AI as Catalyst (FCT Grant 2024.09158.CEECIND) at INET-md | University of Aveiro, Portugal.
"This work was supported by FCT grant 2024.09158.CEECIND"

Credits

Contributor	Role

Hugo Paquete	Principal Investigator, Development, Research
DeepSeek AI	Collaborative development and technical assistance
Open-Meteo	Weather data API
FCT	Funding (Grant 2024.09158.CEECIND)
INET-md	Research institution

Citation

bibtex
@software{Paquete_2026_Weather_Client,
  author = {Paquete, Hugo},
  title = {AEROSONIC Weather Client},
  year = {2026},
  publisher = {GitHub},
  doi = {10.5281/zenodo.20538817},
  url = {https://github.com/HugoPaquete/Aerosonic-weather-client}
}

License
MIT License — Free for commercial and non-commercial use.

Contact
Hugo Paquete, PhD

Email: paquetehugo@gmail.com / hugopaquete@ua.pt
Website: www.hugopaquete.com
GitHub: @HugoPaquete
Institution: University of Aveiro | INET-md

Links
Repository: https://github.com/HugoPaquete/Aerosonic-weather-client
Website: https://www.hugopaquete.com
Documentation: https://github.com/HugoPaquete/Aerosonic-weather-client#readme
DOI: https://doi.org/10.5281/zenodo.20538817

Installation

bash
pip install requests
<div align="center">
AEROSONIC — where data becomes sonic matter.

Built with assistance from DeepSeek AI
© 2026 Hugo Paquete | FCT Grant 2024.09158.CEECIND
AI as Catalyst — INET-md | University of Aveiro

www.hugopaquete.com
