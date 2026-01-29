import os
import telebot
import google.generativeai as genai

# O'zgaruvchilarni tizimdan olamiz (xavfsizlik uchun)
BOT_TOKEN = os.environ.get('8053562841:AAGs73FyVDZbBHOnPADqM-XDQHnFEKpw_og')
GEMINI_KEY = os.environ.get('AIzaSyCtiJGu364xreD6tCn77cKvPnGNEPWNb8k')

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men Gemini 3 botiman. Savolingizni bering!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Xatolik yuz berdi...")

bot.infinity_polling()
