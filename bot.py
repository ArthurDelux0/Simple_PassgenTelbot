import telebot
from telebot import types as t
import random

chars = "1q2w3e4r5t6y7u8i9o0p-[=]azsxdcfvgbhnjmk,l.;/'!@#$%^&*()_+QAWSEDRFTGYHUJIKOLP:{ZXCVBNM"

bot = telebot.TeleBot("Bot token")

@bot.message_handler(commands=["start"])

def start(message):

    markup = t.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    help = t.KeyboardButton("Help")
    use = t.KeyboardButton("Use the bot")

    markup.add(help, use)

    bot.send_message(message.chat.id, f"Hello, {message.from_user.first_name}! You are welcome on PassGen bot main page!", reply_markup=markup)



@bot.message_handler()

def text(message):

    if message.text == "Help":
        bot.send_message(message.chat.id, "Click the 'Use the bot' button, and enter the lenght of a required password.")
    elif message.text == "Use the bot":
        bot.send_message(message.chat.id, "Enter the lenght of a required password")
    else:
        
        d = ""

        for i in range(int(message.text)):
            d += random.choice(chars)
        
        bot.send_message(message.chat.id, f"Your password: {d}")




bot.polling(none_stop=True)
