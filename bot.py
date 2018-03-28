# -*- coding: utf-8 -*-
import telepot
import config
from pprint import pprint
from telepot.loop import MessageLoop

bot = telepot.Bot(config.token)

response = bot.getUpdates()

def handle(msg):
    """ Process request like '3+2' """
    content_type, chat_type, chat_id = telepot.glance(msg)
    text = msg["text"]
    if text=='/help':
         bot.sendMessage(chat_id, "Помощь? Ничего не знаю о таком слове")
    elif text=='/start':
        bot.sendMessage(chat_id, "Ну-с, начнём?")
    else:
     bot.sendMessage(chat_id, "Введите расстояние телепортации\n в километрах:")
     text = int(msg["text"])
     try:
        if (text>0) and (text<=1):
         answer = 'меньше 1ой минуты'
        elif (text>1) and (text<=2):
            answer='Ровно 1 минута '
        elif (text>2) and (text<=3):
            answer='меньше 2х минут '
        elif (text>3) and (text<=5):
            answer='Ровно 2 минуты '
        elif (text>5) and (text<=7):
            answer='Ровно 5 минут '
        elif (text>7) and (text<=9):
            answer='Меньше 7 минут '
        elif (text>9) and (text<=10):
            answer='Ровно 7 минут '
        elif (text>10) and (text<=12):
            answer='Ровно 8 минут '
        elif (text>12) and (text<=18):
            answer='Ровно 10 минут '
        elif (text>18) and (text<=26):
            answer='Ровно 15 минут '
        elif (text>26) and (text<=42):
            answer='Ровно 19 минут '
        elif (text>42) and (text<=65):
            answer='Ровно 22 минуты '
        elif (text>65) and (text<=76):
            answer='Меньше 25 минут '
        elif (text>76) and (text<=81):
            answer='Ровно 25 минут '
        elif (text>81) and (text<=100):
            answer='Ровно 35 минут '
        elif (text>100) and (text<=220):
            answer='Ровно 40 минут '
        elif (text>220) and (text<=250):
            answer='Ровно 45 минут '
        elif (text>250) and (text<=350):
            answer='Ровно 51 минута '
        elif (text>350) and (text<=375):
            answer='Ровно 54 минуты '
        elif (text>375) and (text<=460):
            answer='Ровно 62 минуты '
        elif (text>460) and (text<=500):
            answer='Ровно 65 минут '
        elif (text>500) and (text<=565):
            answer='Ровно 69 минут '
        elif (text>565) and (text<=700):
            answer='Ровно 78 минут '
        elif (text>700) and (text<=800):
            answer='Ровно 84 минуты '
        elif (text>800) and (text<=900):
            answer='Ровно 92 минуты '
        elif (text>900) and (text<=1000):
            answer='Ровно 99 минут '
        elif (text>1000) and (text<=1100):
            answer='Ровно 107 минут '
        elif (text>1100) and (text<=1200):
            answer='Ровно 114 минут '
        elif (text>1200) and (text<1350)  :
            answer='Ровно 117 минут '
        elif (text>=1350):
            answer='Ровно 2 часа '
     
    
        else: answer = 'Повторите попытку'
     except:
        answer = "Необрабатываемая ошибка, подумайте,что вы натворили!)"
    bot.sendMessage(chat_id, "Софтбан: {}".format(answer))


MessageLoop(bot, handle).run_as_thread()

# Keep the program running.
while True:
    n = input('To stop enter "stop":')
    if n.strip() == 'stop':
        break