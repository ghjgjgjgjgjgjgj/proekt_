import json
import requests
import telebot
from telebot import types
import json2
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
access_key = '8b1ee17f-80b6-431c-b9ac-e27f7c6e0dc0'

file = open("works.json", "r", encoding="utf-8")
works = json.load(file)
file.close()

file = open("grafik.json", "r", encoding="utf-8")
grafik = json.load(file)
file.close()

headers = {
    'X-Yandex-Weather-Key': access_key
}
wokrs = []
osad_types = {
    "snow": 'Снег',
    "light-snow": 'Небольшой снег',
    "clear": "Ясно",
    "cloudy": "Облачно",
    "overcast" : "Пасмурно",
    "partly-cloudy":" Переменная облачность",
    "rain": "дождь",
    "light-rain": "легкий дождь"
}

def date_diff(day):
    date_1 = date.today()
    end_date = date_1 + timedelta(days=day)
    return end_date


access_key = 'a82ab972-523c-4643-b46d-5425f05a9c06'

response = requests.get('https://api.weather.yandex.ru/v2/forecast?lat=57.9194&lon=59.965', headers=headers)
pogod = response.json()
data = []

for i in range(7):
    date_1 = pogod['forecasts'][i]['date']
    data.append(date_1)
# print(data)

token = '7086983775:AAF7uz_JgFMI-9xCQhdath-zW99nt5V6ZCg'
bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])
def get_message(message):
    # Если текст полученного сообщения = '/start'
    if message.text == '/start':
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text=data[0], callback_data='1 день')
        button2 = types.InlineKeyboardButton(text=data[1], callback_data='2 день')
        button3 = types.InlineKeyboardButton(text=data[2], callback_data='3 день')
        button4 = types.InlineKeyboardButton(text=data[3], callback_data='4 день')
        button5 = types.InlineKeyboardButton(text=data[4], callback_data='5 день')
        button6 = types.InlineKeyboardButton(text=data[5], callback_data='6 день')
        button7 = types.InlineKeyboardButton(text=data[6], callback_data='7 день')
        keyboard.add(button1,button2,button3,button4,button5,button6,button7)
        bot.send_message(message.from_user.id, text='Привет!',reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    # print('call.data')
    # print(call.data)
    if call.data in['1 день','2 день','3 день' ,'4 день','5 день','6 день','7 день'] :
        day = int(call.data.split(' ')[0]) - 1
        temp = pogod['forecasts'][day]['parts']['day_short']['temp']
        osad = pogod['forecasts'][day]['parts']['day_short']['condition']
        # rabota = grafik["work"]
        # glav = grafik["worker"]
        message_text = ""
        for i in range(len(grafik)):
          # print(type(grafik[i]['date']), type(date_diff(day)), grafik[i]['date'] == date_diff(day))
          if grafik[i]['date'] == str(date_diff(day)):
              message_text = "Температура:" + str(temp) + "\n" + "Осадки:" + osad_types[osad] + "\n" + "Работа:" + grafik[i]["work"]
              break
          else:
              message_text = "Температура:" + str(temp) + "\n" + "Осадки:" + osad_types[osad] + "\n" + "Работа:" + "Работа в этот день не назначена"



        if message_text != '':
            bot.send_message(call.from_user.id, text=message_text)
        else:
            bot.send_message(call.from_user.id, text = "Данные за день не найдены")



























    # if call.data =="2 день":
    #     day = int(call.data.split(' ')[0]) - 1
    #     temp = pogod['forecasts'][day]['parts']['day_short']['temp']
    #     osad = pogod['forecasts'][day]['parts']['day_short']['condition']
    #     if osad in osad_types.keys():
    #         message_text = "Температура:" + str(temp) + "\n" + "Осадки:" + osad_types[osad]+ "\n" + "Работа:"
    #     else:
    #         message_text = "Температура:" + str(temp) + "\n" + "Осадки:" + "Не найдены"+ "\n" + "Работа:"
    #     bot.send_message(call.from_user.id, text=message_text)
    # if call.data =="3 день":
    #     day = int(call.data.split(' ')[0]) - 1
    #     temp = pogod['forecasts'][day]['parts']['day_short']['temp']
    #     osad = pogod['forecasts'][day]['parts']['day_short']['condition']
    #     if osad in osad_types.keys():
    #         message_text = "Температура:" + str(temp) + "\n" + "Осадки:" + osad_types[osad]+ "\n" + "Работа:"
    #     else:
    #         message_text = "Температура:" + str(temp) + "\n" + "Осадки:" + "Не найдены"+ "\n" + "Работа:"
    #     bot.send_message(call.from_user.id, text=message_text)
    # if call.data =="4 день":
    #     day = int(call.data.split(' ')[0]) - 1
    #     temp = pogod['forecasts'][day]['parts']['day_short']['temp']
    #     osad = pogod['forecasts'][day]['parts']['day_short']['condition']
    #
    #     if osad in osad_types.keys():
    #         message_text = "Температура:" + str(temp) + "\n" + "Осадки:" + osad_types[osad]+ "\n" + "Работа:"
    #     else:
    #         message_text = "Температура:" + str(temp) + "\n" + "Осадки:" + "Не найдены"+ "\n" + "Работа:"
    #     bot.send_message(call.from_user.id, text=message_text)
    # if call.data =="5 день":
    #     day = int(call.data.split(' ')[0]) - 1
    #     temp = pogod['forecasts'][day]['parts']['day_short']['temp']
    #     osad = pogod['forecasts'][day]['parts']['day_short']['condition']
    #
    #     if osad in osad_types.keys():
    #         message_text = "Температура:" + str(temp) + "\n" + "Осадки:" + osad_types[osad]+ "\n" + "Работа:"
    #     else:
    #         message_text = "Температура:" + str(temp) + "\n" + "Осадки:" + "Не найдены"+ "\n" + "Работа:"
    #     bot.send_message(call.from_user.id, text=message_text)
    # if call.data =="6 день":
    #     day = int(call.data.split(' ')[0]) - 1
    #     temp = pogod['forecasts'][day]['parts']['day_short']['temp']
    #     osad = pogod['forecasts'][day]['parts']['day_short']['condition']
    #
    #     if osad in osad_types.keys():
    #         message_text = "Температура:" + str(temp) + "\n" + "Осадки:" + osad_types[osad]+ "\n" + "Работа:"
    #     else:
    #         message_text = "Температура:" + str(temp) + "\n" + "Осадки:" + "Не найдены"+ "\n" + "Работа:"
    #     bot.send_message(call.from_user.id, text=message_text)
    # if call.data =="7 день":
    #     day = int(call.data.split(' ')[0]) - 1
    #     temp = pogod['forecasts'][day]['parts']['day_short']['temp']
    #     osad = pogod['forecasts'][day]['parts']['day_short']['condition']
    #
    #     if osad in osad_types.keys():
    #         message_text = "Температура:" + str(temp) + "\n" + "Осадки:" + osad_types[osad]+ "\n" + "Работа:"
    #     else:
    #         message_text = "Температура:" + str(temp) + "\n" + "Осадки:" + "Не найдены"+ "\n" + "Работа:"
    #     bot.send_message(call.from_user.id, text=message_text)
    #
    #
    #
    #

#
bot.polling(non_stop=True, interval=0)
