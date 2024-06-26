import requests
from geopy.geocoders import Nominatim
from prettytable import PrettyTable

def fetch_forecast(latitude, longitude):
    try:
        response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true")
        data = response.json()
        return data['current_weather'] if 'current_weather' in data else None
    except Exception as e:
        print(f"Error fetching weather forecast data: {e}")
        return None

def get_coordinates(city_name):
    try:
        geolocator = Nominatim(user_agent="weather_app")
        location = geolocator.geocode(city_name)
        if location:
            return location.latitude, location.longitude
        else:
            print("Location not found.")
            return None, None
    except Exception as e:
        print(f"Error fetching coordinates: {e}")
        return None, None

def main():
    city_name = input("Enter city name: ")
    latitude, longitude = get_coordinates(city_name)
    if latitude is not None and longitude is not None:
        current_weather = fetch_forecast(latitude, longitude)
        if current_weather:
            table = PrettyTable()
            table.field_names = ["Attribute", "Value"]
            table.add_row(["Time", current_weather['time']])
            table.add_row(["Temperature (°C)", current_weather['temperature']])
            table.add_row(["Wind Speed (m/s)", current_weather['windspeed']])
            table.add_row(["Wind Direction (°)", current_weather['winddirection']])
            table.add_row(["Weather Code", current_weather['weathercode']])
            print(table)
        else:
            print("Failed to fetch weather forecast data.")
    else:
        print("Failed to retrieve coordinates for the specified city.")

if __name__ == "__main__":
    main()
