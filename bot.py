from pyowm import OWM
import telebot
from telebot import types
from pyowm.utils.config import get_default_config
TOKEN = "5071799311:AAGMK4pvN34dbuNem9CbabJIOp0PS5XrVCQ"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['kek'])
def send_welcome(message):
    bot.reply_to(message, "KEKW!")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    board = types.KeyboardButton("Крестики-нолики")
    weather=types.KeyboardButton("Погода⛅")
    markup.add(board,weather)
    bot.reply_to(message, "Привет!",reply_markup=markup)

@bot.message_handler(content_types=['text'])
def new_age(message):
    if message.chat.type == 'private':
        if message.text == 'Погода⛅':
            wea = types.ReplyKeyboardMarkup(resize_keyboard=True)
            UFA = types.KeyboardButton("Уфа")
            SAINT=types.KeyboardButton("Санкт-Петербург")
            wea.add(UFA,SAINT)
            bot.reply_to(message,"Выбери город",reply_markup=wea)      
        elif message.text == 'Крестики-нолики':
            drawer = types.ReplyKeyboardMarkup(resize_keyboard=True)
            board = types.KeyboardButton("Крестики-нолики")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            board1 = types.KeyboardButton("1")
            board2 = types.KeyboardButton("2")
            board3 = types.KeyboardButton("3")
            board4 = types.KeyboardButton("4")
            board5 = types.KeyboardButton("5")
            board6 = types.KeyboardButton("6")
            board7 = types.KeyboardButton("7")
            board8 = types.KeyboardButton("8")
            board9 = types.KeyboardButton("9")
            drawer.add(board1,board2,board3,board4,board5,board6,board7,board8,board9)
            bot.reply_to(message,'Начинаем,ход 1 игрока',reply_markup=drawer)
        elif message.chat.type == 'private':
            if message.text == 'Уфа':
                config_dict = get_default_config()
                config_dict['language'] = 'ru'
                owm = OWM('78f8d6741cc2623ea0c63b430741ca4c',config_dict)
                mgr = owm.weather_manager()
                observation = mgr.weather_at_place('Ufa')
                w = observation.weather
                t = w.temperature("celsius")
                t1 = t['temp']
                t2 = t['feels_like']
                bot.reply_to(message,f"Температура  в  Уфе:  {round(t1)} °C,  {w.detailed_status}.")
            elif message.text == 'Санкт-Петербург':
                config_dict = get_default_config()
                config_dict['language'] = 'ru'
                owm = OWM('78f8d6741cc2623ea0c63b430741ca4c',config_dict)
                mgr = owm.weather_manager()
                observation = mgr.weather_at_place('Saint Petersburg, RU')
                w = observation.weather
                t = w.temperature("celsius")
                t1 = t['temp']
                t2 = t['feels_like']
                bot.reply_to(message,f"Температура  в  Санкт-Петербурге:  {round(t1)} °C,  {w.detailed_status}.")
bot.infinity_polling()

