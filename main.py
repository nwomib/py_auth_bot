import telebot
import requests
from telebot.types import Message

TOKEN = "6036324620:AAGe5-2fuPJJYTtd_DD5jNqRk-_LrWxmWJ"
bot = telebot.TeleBot(TOKEN)

with open("authorized_users.txt", "r") as f:
    authorized_users = [line.strip() for line in f.readlines()]

@bot.message_handler(commands=['start'])
def handle_start(message):
    if message.from_user.username in authorized_users:
        user_id = message.from_user.id
        r = requests.get('https://httpbin.org/get')
        data = r.json()
        ip_address = data['origin']
        bot.reply_to(message, f"Вы авторизованы. Ваш IP-адрес: {ip_address}")
    else:
        bot.reply_to(message, "Вы не авторизованы.")


bot.polling()
