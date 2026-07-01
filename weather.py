import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 40.7128,
    "longitude": -74.0060,
    "current": "temperature_2m,wind_speed_10m,precipitation",
    "temperature_unit": "fahrenheit",
}

response = requests.get(url, params=params)
print(response.status_code)
print(response.headers)
print(response.url)
print(type(response.json()))

data = response.json()
print(data.keys())
print(data["current"].keys())
print(data["current_units"])


current = data['current']
print(f"Temp: {current['temperature_2m']}°F")
print(f"Wind: {current['wind_speed_10m']} mph")
print(f"Current precipitation: {current['precipitation']}")
