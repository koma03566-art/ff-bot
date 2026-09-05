import telebot
import requests
import json
from telebot import types
from datetime import datetime

TOKEN = "86808162492:AAG8ozKV7ORaCD2tcOe-OdEvnf1OS72zrwk"
ADMIN_ID = 7971355281
ORDERS_FILE = "orders.json"
BOT_NAME = "🔥 FF ДОНАТ БОТ 🔥"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("💎 Алмаз сатып алуу")
    btn2 = types.KeyboardButton("📞 Колдоо")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f"Салам! {BOT_NAME} кош келдиң!\nАлмаз заказ кылуу үчүн баскычты бас", reply_markup=markup)

print("Бот иштеп жатат...")
bot.polling(none_stop=True)
