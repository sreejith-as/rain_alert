# ☁️ Telegram Weather Alert Bot

A Python script that checks the weather forecast using the OpenWeatherMap API and sends a **Telegram alert** if it's likely to rain.  
It’s perfect for personal daily notifications and runs securely using environment variables.

---

## 🚀 Features

- 🌧️ Detects upcoming rain based on 3-hour forecast data
- 📲 Sends an automated message to your Telegram account
- 🔐 Uses a `.env` file to keep API keys safe
- ⏰ Can be scheduled to run daily (via cron or Python `schedule`)

---

## 📦 Technologies Used

- **Python 3.13.3**
- [OpenWeatherMap API](https://openweathermap.org/api)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- `requests`, `python-dotenv`,

---

## 📁 Project Structure

```

rain_alert/
├── main.py         # Main script
├── .env                     # Contains your secret API keys (NOT pushed to GitHub)
├── .gitignore               # Ignores .env and other sensitive files
├── requirements.txt         # Python dependencies
└── README.md

````

---

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/sreejith-as/rain_alert.git
cd weather-alert-bot
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up `.env` file

Create a `.env` file in the root directory:

```env
TELEGRAM_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
WEATHER_API_KEY=your_openweathermap_api_key
LATITUDE= your_latitude_here
LONGITUDE= your_longitude_here
```

> ⚠️ **Do not share or commit this file** – it contains your private tokens.

### 4. Run the script

```bash
python weather_alert.py
```

---

## ⏰ Automate with Scheduling

### Option A: Use `cron` (Linux/macOS)

Run daily at 7 AM:

```cron
0 7 * * * /usr/bin/python3 /full/path/to/weather_alert.py
```

### Option B: Use Python's `schedule` (Cross-platform)

Uncomment the schedule section in `weather_alert.py`, install the module:

```bash
pip install schedule
```

And let the script run in the background.

---

## 📬 How It Works

* Calls the OpenWeatherMap API for the next 12 hours (4 intervals of 3 hours)
* If any condition code indicates rain (code < 700), it sends a Telegram message
* Example alert:
  `"It's going to rain today. Remember to bring an umbrella! ☔"`

---

## 📄 License

MIT License © 2025 [Sreejith A S](https://github.com/sreejith-as)

---

## 🙋‍♂️ Author

**Sreejith A S**
📍 Kerala, India
🔗 [LinkedIn](www.linkedin.com/in/sreejith-a-sreenivasan)
📧 [sreejithsreenivasan.06@gmail.com](mailto:sreejithsreenivasan.06@gmail.com)

---

## 💬 Feedback

Have an idea or improvement? Feel free to open an issue or send a message!

