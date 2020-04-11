import time
import telebot
import requests

TOKEN = '872866013:AAHN9cVb5Ve_ztGhlrFlq-4iUvKj7yGo9uw' # change the token of your own bot
bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start']) # welcome message handler
def send_welcome(message):
    bot.reply_to(message, 'Hello here is your daily dose of happiness! :D Click on me! /woof or /meow ')

@bot.message_handler(commands=['help']) # help message handler
def send_help(message):
    bot.reply_to(message, 'ALPHA = FEATURES MAY NOT WORK')

# retrieve dog photo from the api
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

# retrieve cat photo from the api
def get_cat_url():
    contents = requests.get('http://aws.random.cat/meow').json()
    url = contents['file']
    return url


@bot.message_handler(commands=['woof']) # help message handler
def send_photo(message):
    url = get_url()
    bot.reply_to(message, url)

@bot.message_handler(commands=['meow']) # help message handler
def send_cat_photo(message):
    url = get_cat_url()
    bot.reply_to(message, url)

while True:
    try:
        bot.polling(none_stop=True)
        # ConnectionError and ReadTimeout because of possible timout of the requests library
        # maybe there are others, therefore Exception
    except Exception:
        time.sleep(15)
