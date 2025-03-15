import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "your_api_key_here"  # Replace with your OpenWeather API Key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return

    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data["cod"] == 200:
        weather_info.set(f"City: {data['name']}\n"
                         f"Temperature: {data['main']['temp']}°C\n"
                         f"Humidity: {data['main']['humidity']}%\n"
                         f"Wind Speed: {data['wind']['speed']} m/s\n"
                         f"Weather: {data['weather'][0]['description'].title()}")
    else:
        messagebox.showerror("Error", "City not found!")

# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("300x300")

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=10)

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=5)

weather_info = tk.StringVar()
weather_label = tk.Label(root, textvariable=weather_info, justify="left")
weather_label.pack(pady=10)

root.mainloop()
