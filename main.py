import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

HOTELS = {
    "5stars": "🏨 5 Stars - In front of Haram\n\n1. Fairmont Makkah - 450€ / nuit\n2. Hilton Makkah - 380€ / nuit\n3. Raffles Makkah - 520€ / nuit",
    "4stars": "🏨 4 Stars\n\n1. Elaf Kinda - 180€ / nuit\n2. Al Marwa Rayhaan - 210€ / nuit\n3. Swissotel Al Maqam - 230€ / nuit",
    "eco": "🏨 Economic - Shuttle to Haram\n\n1. Al Kiswah Towers - 65€ / nuit\n2. Le Meridien Towers - 80€ / nuit\n3. Al Tayseer Towers - 55€ / nuit"
}

@bot.message_handler(commands=['start'])
def start(m):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("5 Stars - In front of Haram", callback_data="5stars"))
    markup.add(InlineKeyboardButton("4 Stars", callback_data="4stars"))
    markup.add(InlineKeyboardButton("Economic - Shuttle to Haram", callback_data="eco"))
    bot.send_message(m.chat.id, "أهلا بيك في بوت فنادق مكة 🕋\nخير الفئة:", reply_markup=markup)

@bot.callback_query_handler(func=lambda c: True)
def answer(c):
    bot.send_message(c.message.chat.id, HOTELS[c.data] + "\n\nللحجز ابعث: الاسم + التاريخ + عدد الليالي")

bot.infinity_polling()
