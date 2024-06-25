import tkinter as tk
from tkinter import messagebox
import requests
from geopy.geocoders import Nominatim

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

def display_weather(current_weather):
    if current_weather:
        weather_info = "\n".join([f"{key.replace('_', ' ').title()}: {value}" for key, value in current_weather.items()])
        weather_info_label.config(text=weather_info)
    else:
        weather_info_label.config(text="Failed to fetch weather data.")

def get_weather():
    city_name = entry.get()
    latitude, longitude = get_coordinates(city_name)
    if latitude is not None and longitude is not None:
        current_weather = fetch_forecast(latitude, longitude)
        display_weather(current_weather)
    else:
        messagebox.showerror("Error", "Failed to retrieve coordinates for the specified city.")

# GUI setup
root = tk.Tk()
root.title("Current Weather App")

frame = tk.Frame(root)
frame.pack(pady=20)

label = tk.Label(frame, text="Enter city name:")
label.grid(row=0, column=0)

entry = tk.Entry(frame)
entry.grid(row=0, column=1)

button = tk.Button(frame, text="Get Weather", command=get_weather)
button.grid(row=0, column=2)

weather_info_frame = tk.Frame(root, bd=2, relief=tk.GROOVE)
weather_info_frame.pack(padx=10, pady=10)

weather_info_label = tk.Label(weather_info_frame, text="", justify=tk.LEFT)
weather_info_label.pack()

root.mainloop()
