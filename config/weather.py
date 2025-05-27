import requests

def get_weather(latitude, longitude, date):
# Construir la URL de Open-Meteo
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": "Europe/Madrid",
        "start_date": date,
        "end_date": date
    }

    # Hacer la petición a la API externa
    response = requests.get(url, params=params)
    data = response.json()

    # Extraer los datos de temperatura
    daily = data.get("daily", {})
    t_max = daily.get("temperature_2m_max", [None])[0]
    t_min = daily.get("temperature_2m_min", [None])[0]
    precipitation = daily.get("precipitation_sum", [None])[0]

    return {
        "temperature_max": t_max,
        "temperature_min": t_min,
        "precipitation": precipitation
    }