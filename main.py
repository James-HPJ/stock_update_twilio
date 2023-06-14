import requests
import datetime as dt
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()


account_sid = os.environ["TWILIO_ACC_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = os.environ["A_VANTAGE_APIKEY"]

date_yesterday = dt.datetime.now().date() - dt.timedelta(days=1)
date_before_yest = date_yesterday - dt.timedelta(days=1)

stock_api_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": API_KEY,
}

response = requests.get(f"https://www.alphavantage.co/query", params=stock_api_params)
data = response.json()

tsla_close_price_yest = float(
    data["Time Series (Daily)"][date_yesterday.strftime("%Y-%m-%d")]["4. close"]
)
tsla_close_price_db_yest = float(
    data["Time Series (Daily)"][date_before_yest.strftime("%Y-%m-%d")]["4. close"]
)

percentage_change = (
    (tsla_close_price_yest - tsla_close_price_db_yest) / tsla_close_price_yest * 100
)

if percentage_change <= -1 or percentage_change >= 1:
    rounded_2places = round(percentage_change, 2)

    NEWS_API_KEY = os.environ["NEWS_APIKEY"]
    news_api_params = {"q": COMPANY_NAME, "apiKey": NEWS_API_KEY}

    news_response = requests.get(
        "https://newsapi.org/v2/everything", params=news_api_params
    )
    news_data = news_response.json()["articles"]

    news_to_send = []

    arrow_symbol = "🔺" if rounded_2places >= 0 else " 🔻"

    for i in range(0, 3):
        article = news_data[i]
        news_to_send.append(
            f"Headline: {article['title']}  \nBrief: {article['description']}"
        )

    body_to_send = " ".join(news_to_send)

    message = client.messages.create(
        from_=f"whatsapp:{os.environ['TWILIO_NO']}",
        body=f"{STOCK}: {arrow_symbol}{rounded_2places}%\n{body_to_send}",
        to=f"whatsapp:{os.environ['YOUR_WHATSAPP_NO']}",
    )
