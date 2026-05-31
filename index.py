import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "48ad575823304b843c10240f42096339"

def get_weather():
    city = city_entry.get()

    if not city:
        messagebox.showwarning("Warning", "Enter city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        print(data)  # DEBUG

        if str(data.get("cod")) != "200":
            result_label.config(text="City not found or API issue")
            return

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]

        result_label.config(
            text=f"{city}\n\nTemperature: {temp}°C\nCondition: {desc}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

title = tk.Label(root, text="Weather App", font=("Arial", 20))
title.pack(pady=15)

city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=10)

btn = tk.Button(root, text="Get Weather", command=get_weather)
btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 13))
result_label.pack(pady=20)

root.mainloop()