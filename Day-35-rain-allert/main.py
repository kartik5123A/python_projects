import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
# import pywhatkit

load_dotenv()

weather_params = {
    "lat" : 26.921806,
    "lon" : 75.842183,
    "appid" : os.getenv("API_KEY"),
    "cnt" : 4
}

response = requests.get(os.getenv("OWM_ENDPOINT"), params = weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

bring_umbrella = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
       bring_umbrella = True

if bring_umbrella == True:
    
    # at text message

    # message = "Boy!! It's gonna be rain today. Be sure to bring an umbrella"
    # client = Client(account_sid, auth_token)
    # message = client.messages \
    #                 .create(
    #                     body= message,
    #                     from_='+15085939891',
    #                     to='+915454541642'
    #                 )
    # print(message.status)


    # at telegram

    bot_message = "Boy!! It's gonna be rain today. Be sure to bring an umbrella"
    send_text = "https://api.telegram.org/bot" + os.getenv("BOT_TOKEN") + "/sendMessage?chat_id=" + os.getenv("BOT_CHATID") + "&parse_mode=Markdown&text=" + bot_message
    response_2 = requests.get(send_text)


    # at whatsapp

    # pywhatkit.sendwhatmsg("+91766454323", "Konichiwa", 21, 10)

else :
    print("Bhai chaleja aise hi, aaj safe h.")    