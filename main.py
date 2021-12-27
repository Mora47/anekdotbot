import telebot
from telebot import types
from config import token
from bs4 import BeautifulSoup
from tools import filter, randomInt, hrefFilter, randomPage
import requests
bot = telebot.TeleBot(token)
def main():
    url = randomPage('https://4tob.ru/anekdots/page')
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    res = str(soup.find_all("div", class_="text")).split('''<div class="text">''')
    while True:
        num = randomInt(res)
        if(hrefFilter(res[num])):
            res = filter(res[num])
            break
    return res

@bot.message_handler(commands = ['start'])
def next(message):
    markup_reply= types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_next = types.KeyboardButton('Показать анекдот')
    markup_reply.add(button_next)
    bot.send_message(message.chat.id, '''Нажми: "Показать анекдот" ''', reply_markup = markup_reply)

@bot.message_handler(content_types = ['text'])
def answer(message):
    if message.text == 'Показать анекдот':
        ans = main()
        print(ans)
        bot.send_message(message.chat.id, ans)

bot.polling(none_stop = True, interval = 0)
