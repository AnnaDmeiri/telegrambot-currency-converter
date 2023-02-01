import telebot
TOKEN ="5498979614:AAHuNcajJNfzdSrUnjP50BpPrB1IC4QFziM"

bot = telebot.TeleBot("5498979614:AAHuNcajJNfzdSrUnjP50BpPrB1IC4QFziM")


@bot.message_handler(commands=['start', 'help'])
def repeat(message: telebot.types.Message):
    bot.reply_to(message, f'Приветствую, {message.chat.username}')


@bot.message_handler(content_types=['voice',])
def repeat(message: telebot.types.Message):
    bot.send_message(message.chat.id, "У тебя очень приятный голос!")


@bot.message_handler(content_types=['text', ])
def repeat(message: telebot.types.Message):
    bot.send_message(message.chat.id, "Давай пообщаемся, я очень рад!")


# @bot.message_handler(content_types=['photo',])
# def repeat(message: telebot.types.Message):
#     bot.send_message(message.chat.id, "Вау, ну какава красата!")


@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Мне нравится!')


@bot.message_handler(commands=['start', 'help'])
def repeat(message: telebot.types.Message):
    bot.reply_to(message, f'Приветствую, {message.chat.username}')


bot.polling(none_stop=True)


import requests
import lxml.html
from lxml import etree

html = requests.get('https://www.python.org/').content

tree = lxml.html.document_fromstring(html)
title = tree.xpath('/html/head/title/text()')

print(title)

import requests
import lxml.html
from lxml import etree
tree = etree.parse('Welcome to Python.org.html',
                   lxml.html.HTMLParser())

ul = tree.findall('body/div[1]/div[3]/div/section/div[2]/div[1]/div/ul/li')

for li in ul:
    a = li.find('a')
    print(a.text)

