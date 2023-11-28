import telebot 

from env import BOT_TOKEN
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['info'])
def info(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Привет,! Я бот. Версия, которая ничего не умеет.")
bot.polling()

# @bot.message_handler()
# def start(message: telebot.types.Message):
#     bot.send_message(message.chat.id, message.text)
# bot.polling()
