import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 40.7128,
    "longitude": -74.0060,
    "current": "temperature_2m,wind_speed_10m",
    "temperature_unit": "fahrenheit"
}

response = requests.get(url, params=params)

print(response.status_code)

data = response.json()


current = data['current']
print(f"Temp: {current['temperature_2m']}°F")
print(f"Wind: {current['wind_speed_10m']} mph")
