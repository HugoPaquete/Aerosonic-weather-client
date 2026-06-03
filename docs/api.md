# API Reference

## WeatherClient

### `fetch() -> WeatherData`
Returns current weather data for selected city.

### `set_city(city: str) -> bool`
Changes current city. Returns True if city exists.

### `get_cities() -> List[str]`
Returns list of all available cities.

## WeatherData

| Attribute | Type | Description |
|:---|:---|:---|
| temperature | float | °C |
| wind_speed | float | km/h |
| city | str | City name |
| source | str | Data source |
