# AEROSONIC Weather Client

> Free and open-source Python weather client. Fetches real-time meteorological data from Open-Meteo API with procedural fallback and automatic normalization.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Requests](https://img.shields.io/badge/requests-2.28+-green.svg)](https://requests.readthedocs.io/)
[![FCT](https://img.shields.io/badge/FCT-2024.09158.CEECIND-blue.svg)](https://www.fct.pt)
[![INET-md](https://img.shields.io/badge/INET-md-University%20of%20Aveiro-purple.svg)](https://www.inetmd.pt)
[![DeepSeek](https://img.shields.io/badge/DeepSeek-AI%20Assisted-orange.svg)](https://deepseek.com)
[![Website](https://img.shields.io/badge/website-hugopaquete.com-1e3a8a.svg)](https://www.hugopaquete.com)

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
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

---

## Features

| Category | Description |
|:---|:---|
| Real-time weather data | Temperature, wind speed, precipitation |
| 12+ cities included | Lisbon, London, Tokyo, New York, etc. |
| Simple caching | 5 seconds TTL to reduce API calls |
| Procedural fallback | Works even when API fails |
| Automatic normalization | 0-1 range for ML and sonification |
| Minimal dependencies | Only requires requests library |

## Funding
This project is part of AI as Catalyst (FCT Grant 2024.09158.CEECIND) at INET-md | University of Aveiro, Portugal.
"This work was supported by FCT grant 2024.09158.CEECIND"

## Credits

Hugo Paquete	Principal Investigator, Development, Research

DeepSeek AI	Collaborative development and technical assistance

Open-Meteo	Weather data API

FCT	Funding (Grant 2024.09158.CEECIND)

INET-md	Research institution

## License
MIT License — Free for commercial and non-commercial use.

## Contact
Hugo Paquete, PhD
Email: paquetehugo@gmail.com / hugopaquete@ua.pt

Website: www.hugopaquete.com

GitHub: @HugoPaquete

Institution: University of Aveiro | INET-md

Links
Repository: https://github.com/HugoPaquete/Aerosonic-weather-client

Website: https://www.hugopaquete.com

Documentation: https://github.com/HugoPaquete/Aerosonic-weather-client#readme

---

## Installation

```bash
pip install requests

Citation
bibtex
@software{Paquete_2026_Weather_Client,
  author = {Paquete, Hugo},
  title = {AEROSONIC Weather Client},
  year = {2026},
  url = {https://github.com/HugoPaquete/Aerosonic-weather-client}
}
