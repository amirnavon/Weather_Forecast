import streamlit as st
import requests
import datetime as dt


def get_weather(city):
    """
    This function gets a city name and returns uptodate data from the online service 'openweathermap'.
    Data contains locations' UTC date and time, weather, temperature, humidity.
    :return: text to display
    :rtype: string
    """
    api_key = 'a2ea41563a89e46d5877cb84f24215d5'
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    )
    # if no info response from openweathermap
    if weather_data.json()['cod'] == '404':
        return "No City Found, try different location"
    else:
        location_timezone = dt.timezone(dt.timedelta(seconds=int(weather_data.json()['timezone'])))
        formatted_location_timezone = dt.datetime.now(tz=location_timezone).strftime("%m/%d/%Y, %H:%M:%S")
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        humidity = weather_data.json()['main']['humidity']
        return (f"It is {formatted_location_timezone} in {city.capitalize()} and the weather now is {weather}, "
                f"\ntemperature is {temp}\u00b0C and humidity is {humidity}.")


def main():
    """
    This is the main function of 'GET WEATHER APP'. A user is asked for city name, and city info is displayed via
    'openweathermap' webpage integration. Functionality is 'streamlit' platform adjusted.
    :return: weather_info
    :rtype: string
    """
    # Page header
    st.header("Welcome to GET WEATHER APP")
    # User input
    city_input = st.text_input("Enter city name: ")
    # Run function only after user input
    if city_input:
        weather_info = st.write(get_weather(city_input))
        if weather_info:
            st.write(weather_info)
    # Default sentence
    else:
        st.write("Please enter a city name to get the weather.")


if __name__ == "__main__":
    main()
