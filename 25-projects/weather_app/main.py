import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
API_KEY = os.getenv("TOMORROW_API_KEY")

# Custom CSS for professional UI
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .stApp {
            background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        }
        .main-title {
            font-size: 2.5rem;
            font-weight: bold;
            color: #f8b400;
            text-align: center;
        }
        .weather-box {
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(255, 255, 255, 0.1);
            text-align: center;
        }
        .metric-box {
            font-size: 1.2rem;
            font-weight: bold;
            color: #ffffff;
            padding: 10px;
        }
        .footer {
            text-align: center;
            font-size: 12px;
            margin-top: 50px;
            color: #ccc;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='main-title'>🌤️ Professional Weather App</h1>", unsafe_allow_html=True)

# Input Field for City
city = st.text_input("📍 Enter City Name", "Karachi")

# Fetch Weather Data Function
def get_weather(city):
    url = f"https://api.tomorrow.io/v4/weather/realtime?location={city}&apikey={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

# Display Weather Data
if st.button("🔍 Get Weather"):
    weather_data = get_weather(city)

    if weather_data:
        temp = weather_data['data']['values']['temperature']
        humidity = weather_data['data']['values']['humidity']
        wind_speed = weather_data['data']['values']['windSpeed']

        # Weather Box
        st.markdown("<div class='weather-box'>", unsafe_allow_html=True)

        # Display Metrics
        st.markdown(f"<div class='metric-box'>🌡️ Temperature: {temp}°C</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='metric-box'>💧 Humidity: {humidity}%</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='metric-box'>💨 Wind Speed: {wind_speed} km/h</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.error("❌ City not found or API issue. Try again!")

# Footer
st.markdown("<div class='footer'>Made with ❤️ by You</div>", unsafe_allow_html=True)
