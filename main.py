import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# === CONFIG ===
TOKEN = os.getenv("TELEGRAM_TOKEN") # Telegram bot token
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID") # Your Telegram user ID or group chat ID
API_KEY = os.getenv("WEATHER_API_KEY") # OpenWeatherMap API key

# Alert message to send if rain is expected
message = "It's going to rain today. Remember to bring an umbrella! ☔"

# Telegram API endpoints for sending messages

send_message_endpoint = (
    f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    f"?chat_id={CHAT_ID}&text={message}"
)

# OpenWeatherMap API endpoint and location
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
weather_parameters = {
    "lat": os.getenv("LATITUDE"), # Your Latitude from .env
    "lon": os.getenv("LONGITUDE"), # Your Longitude from .env
    "appid": API_KEY,
    "cnt": 4,
}

# === FETCH WEATHER DATA ===
response = requests.get(OWM_ENDPOINT, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()

# === CHECK FOR RAIN ===
will_rain = False

# Loop through the upcoming 4 forecasts (3-hour intervals)
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    print(f"Weather condition code: {condition_code}")
    
    # Weather codes < 700 usually mean rain, snow, or other precipitation
    if int(condition_code) < 700:
        will_rain = True

# === SEND TELEGRAM ALERT IF NEEDED ===
if will_rain:
    response = requests.get(send_message_endpoint)
    print("Rain alert sent via Telegram.")
else:
    print("No rain expected.")
