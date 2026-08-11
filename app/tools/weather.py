import requests
from langchain_core.tools import tool

@tool
def get_weather(city: str) -> str:
    """Get current weather for a supported city."""
    coordinates = {
        "pune": (18.5204, 73.8567),
        "mumbai": (19.0760, 72.8777),
        "delhi": (28.6139, 77.2090),
        "bangalore": (12.9716, 77.5946),
        "hyderabad": (17.3850, 78.4867),
    }

    key = city.lower().strip()
    if key not in coordinates:
        return f"I don't have coordinates configured for {city}."

    latitude, longitude = coordinates[key]
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,weather_code"
        },
        timeout=5
    )
    response.raise_for_status()
    current = response.json()["current"]

    return (
        f"Weather in {city.title()}: "
        f"{current['temperature_2m']}°C, "
        f"humidity {current['relative_humidity_2m']}%"
    )
