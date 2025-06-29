import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Function to fetch weather data
def fetch_weather_data(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}"
    response = requests.get(complete_url)
    return response.json()

# Function to extract relevant data
def extract_weather_info(data):
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        return {
            "Temperature (C)": main["temp"] - 273.15,  # Convert Kelvin to Celsius
            "Pressure (hPa)": main["pressure"],
            "Humidity (%)": main["humidity"],
            "Description": weather["description"]
        }
    else:
        return None

# Main execution for Streamlit dashboard
st.title("Weather Dashboard")

api_key = "8151fd19e651a96ebe3e427717592b3a"
city = st.text_input("Enter city name:")
if st.button("Get Weather"):
    weather_data = fetch_weather_data(city, api_key)
    weather_info = extract_weather_info(weather_data)
    
    if weather_info:
        st.write(weather_info)
        
        # Sample data for visualization
        data = {
            "Temperature (C)": [weather_info["Temperature (C)"]],
            "Humidity (%)": [weather_info["Humidity (%)"]],
        }
        
        df = pd.DataFrame(data)
        
        # Create a bar plot
        st.bar_chart(df)
    else:
        st.error("City Not Found")
