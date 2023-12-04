import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

from env import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['info'])
def info(message: telebot.types.Message):
    bot.send_message(message.chat.id, "Привет! Я бот. Версия, которая ничего не умеет.")


@bot.message_handler(commands=['dog_1'])
def send_photo(message: telebot.types.Message):
    pic = open(r'C:\Users\77083\Desktop\dog.jpg', 'rb')
    bot.send_photo(message.chat.id, pic, 'Собакен')


@bot.message_handler(commands=['dog_2'])
def send_photo(message: telebot.types.Message):
    bot.send_photo(
        message.chat.id,
        "https://placedog.net/866",
        caption="Собака из ссылки"
    )


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    user = message.from_user
    bot.send_message(message.chat.id, f"Привет, {user.first_name}! Выберите опцию:")

    keyboard = [
        [InlineKeyboardButton("GitHub", url="https://github.com")],
        [InlineKeyboardButton("Balance", callback_data='balance')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(message.chat.id, 'Выберите:', reply_markup=reply_markup)


@bot.callback_query_handler(func=lambda call: True)
def balance(call):
    query = call.data

    if query == 'balance':
        balance_keyboard = [
            [InlineKeyboardButton("Вывод", callback_data='withdraw')],
            [InlineKeyboardButton("Пополнить", callback_data='topup')],
        ]

        balance_markup = InlineKeyboardMarkup(balance_keyboard)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Выберите действие:', reply_markup=balance_markup)


bot.polling()
