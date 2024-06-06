import streamlit as st
import pandas as pd
import requests
from datetime import datetime
import pytz

api_key = 'a2ea41563a89e46d5877cb84f24215d5'

city_input = input("Enter city name: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city_input}&appid={api_key}"
)

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    humidity = weather_data.json()['main']['humidity']
    print(f"The weather now in {city_input.capitalize()} is {weather}, "
          f"temperature is {temp}\u00b0F and humidity is {humidity}."
          )


