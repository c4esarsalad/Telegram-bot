import telebot
from bot_logic import gen_pass
from coin_game import gen_emodji
from coin_game import flip_coin

bot = telebot.TeleBot("---")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Напиши команду /get_password чтобы я сделал тебе пароль")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['get_password'])
def send_hello(message):
    bot.reply_to(message, gen_pass(10))

@bot.message_handler(commands=['game'])
def send_hello(message):
    bot.reply_to(message, gen_emodji())

@bot.message_handler(commands=['coin'])
def send_hello(message):
    bot.reply_to(message, flip_coin())
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
print("Бот запущен!")

bot.polling()