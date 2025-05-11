import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "964fb10f37704fa4a37184629251105 " 
BASE_URL = "https://api.weatherapi.com/v1/current.json"

def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    params = {"key": API_KEY, "q": city}
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if "error" in data:
            messagebox.showerror("Error", data["error"]["message"])
        else:
            location = f"{data['location']['name']}, {data['location']['region']}, {data['location']['country']}"
            condition = data["current"]["condition"]["text"]
            temp = f"{data['current']['temp_c']} °C"
            humidity = f"{data['current']['humidity']}%"
            wind = f"{data['current']['wind_kph']} kph"

            result_text.set(
                f"📍 Location: {location}\n"
                f"🌤️ Condition: {condition}\n"
                f"🌡️ Temperature: {temp}\n"
                f"💧 Humidity: {humidity}\n"
                f"💨 Wind Speed: {wind}"
            )
    except requests.exceptions.RequestException:
        messagebox.showerror("Network Error", "Could not connect to the weather service.")

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 12), justify="center")
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12), bg="lightblue").pack(pady=10)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, font=("Arial", 11), justify="left", wraplength=380).pack(pady=10)

root.mainloop()
