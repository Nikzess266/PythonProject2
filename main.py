import telebot
from telebot import types
from telegram import Update
#from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext

bot = telebot.TeleBot('8019696712:AAEgtdeWDrJXJVEOBS3FPuyp6_zpljfWIrQ')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('VIP меню⭐️')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Меню🔑')
    btn3 = types.KeyboardButton('Настройки⚙️')
    markup.row(btn2, btn3)
    btn4 = types.KeyboardButton('Ошибки и баги🚫')
    btn5 = types.KeyboardButton('ChatGPT🛜')
    markup.row(btn4, btn5)
    btn6 = types.KeyboardButton('Промокоды🔱')
    btn7 = types.KeyboardButton('Приложение YouTube🌏')
    markup.row(btn6, btn7 )
    bot.send_message(message.chat.id, f'Здраствуйте! Добро пожаловать в наш телеграм бот! Чем я вам могу помочь?', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'VIP меню⭐️':
        bot.send_message(message.chat.id,'Вы открыли вкладку VIP меню, пожалуйста, прежде чем пользоваться этой функцией, вам нужно заплатить 99 рублей. С функцией "VIP меню" вы получаете: ранний доступ к привью; ранний доступ к монтажу видео; получать самые свежие новости нашего канала и проекта RaidMine; возможность присутствия на стримах и в видеороликах; доступ к нашим контактам (VK, Discord, Telegram). VIP меню действует только 1 месяц, по этому используйте её с пользой!!!')
        markup = types.ReplyKeyboardMarkup()
        btn8 = types.KeyboardButton('Да✅')
        btn9 = types.KeyboardButton('Нет🚫')
        markup.row(btn8, btn9)
        bot.send_message(message.chat.id, 'Хотите приобрести этот товар?', reply_markup=markup)
    elif message.text == 'Да✅':
        bot.send_message(message.chat.id, 'бебебе')





@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Здраствуйте, добро пожаловать в бот WoodVarden, чем я могу вам помочь?')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}')


@bot.message_handler(commands=['vip'])
def main(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}')

@bot.message_handler(commands=['video'])
def main(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}')

@bot.message_handler()
def info(message):
    if message.text.lower() == ():
        bot.send_message(message.chat.id, f'Данной команды не существует, {message.from_user.first_name}')

bot.polling(none_stop=True)