# -*- coding: utf-8 -*-
import telebot
import urllib
import os
import sys
from parser import image_url

# Initialize the bot with its token. Remember to replace bot_token_here with
# your bot token. You need to talk to @BotFather to get one.

bot = telebot.TeleBot("237899070:AAFv8olIa1DFfzQSZ0G7sa-8fV_T7mHhEuk")

# Handler for command start. It returns a welcome message to the chat.

@bot.message_handler(commands=['start'])
def welcome_message(message):
    msg = 'This is amatuer project. It\'s subject to change w/o any further notice. For command list, use /help.'
    bot.send_message(message.chat.id, msg)

# Handler for help command. It returns some help to the user.

@bot.message_handler(commands=['help'])
def help_message(message):
    msg = 'Type /menu command to get business lunch menu from Paulaner-brauhaus'
    bot.send_message(message.chat.id, msg)

# Handler for help command. It returns some help to the user.

@bot.message_handler(commands=['menu'])
def menu_message(message):
    url = image_url()
    bot.send_message(message.chat.id, str(url))

# This function keeps the connection to the Telegram Bot API alive and does all
# the neccesary operations to send the data. none_stop=True prevents the script
# from crashing if API errors occur.

bot.polling(none_stop=True)