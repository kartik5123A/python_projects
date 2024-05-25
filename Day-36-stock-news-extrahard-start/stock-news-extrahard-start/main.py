import requests
from datetime import date, timedelta
from twilio.rest import Client
import os
from dotenv import load_dotenv

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

load_dotenv()

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : os.getenv("API_KEY_STOCK")
}

news_params = {
    "qInTitle" : COMPANY_NAME,
    "apiKey" : os.getenv("API_KEY_NEWS"),
    "sortBy" : "publishedAt"
}

stock_response = requests.get(os.getenv("STOCK_API"), stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]

yesterday_data = stock_data_list[0]
yesterday_closing_data = yesterday_data["4. close"]

day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing_data = day_before_yesterday_data["4. close"]

difference = (float(yesterday_closing_data) - float(day_before_yesterday_closing_data))

percent_change = (difference / float(yesterday_closing_data)) * 100

news_response = requests.get(os.getenv("NEWS_API"), news_params)
news_response.raise_for_status()
articles = news_response.json()["articles"]
three_articles = articles[:3]

if difference < 0:
    percent_change = -percent_change
    news = [f"{STOCK} : 🔻{int(percent_change)}% \n\nHeadline: {article['title']}. \n\nBrief: {article['description']}" for article in three_articles]

else:
    news = [f"{STOCK} : 🔺{int(percent_change)}% \n\nHeadline: {article['title']}. \n\nBrief: {article['description']}" for article in three_articles]


for article in news:
    bot_message = article
    send_text = "https://api.telegram.org/bot" + os.getenv("BOT_TOKEN") + "/sendMessage?chat_id=" + os.getenv("BOT_CHATID") + "&parse_mode=Markdown&text=" + bot_message
    response = requests.get(send_text)   