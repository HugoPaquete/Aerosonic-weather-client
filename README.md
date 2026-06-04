# AEROSONIC Weather Client

> Free and open-source Python weather client. Fetches real-time meteorological data from Open-Meteo API with procedural fallback and automatic normalization.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Requests](https://img.shields.io/badge/requests-2.28+-green.svg)](https://requests.readthedocs.io/)
[![FCT](https://img.shields.io/badge/FCT-2024.09158.CEECIND-blue.svg)](https://www.fct.pt)
[![INET-md](https://img.shields.io/badge/INET-md-University%20of%20Aveiro-purple.svg)](https://www.inetmd.pt)
[![DeepSeek](https://img.shields.io/badge/DeepSeek-AI%20Assisted-orange.svg)](https://deepseek.com)
[![Website](https://img.shields.io/badge/website-hugopaquete.com-1e3a8a.svg)](https://www.hugopaquete.com)

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Basic Usage](#basic-usage)
- [Change City](#change-city)
- [Available Cities](#available-cities)
- [Normalized Values](#normalized-values)
- [Normalization Bounds](#normalization-bounds)
- [Manual Mode](#manual-mode-testing)
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

---

## Features

| Feature | Description |
|:---|:---|
| Real-time weather data | Temperature, wind speed, precipitation |
| 12+ cities included | Lisbon, London, Tokyo, New York, etc. |
| Simple caching | 5 seconds TTL to reduce API calls |
| Procedural fallback | Works even when API fails |
| Automatic normalization | All values normalized to 0-1 range |
| Minimal dependencies | Only requires requests library |

---

## Installation

### Using pip (after PyPI release)

```bash
pip install aerosonic-weather
