import requests

api_key = ''

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}"
)

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    humidity = weather_data.json()['main']['humidity']
    print(f"The weather now in {user_input.capitalize()} is {weather}.\nthe temperature is {temp} \u00b0F\nand the "
          f"humidity is {humidity}")