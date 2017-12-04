# -*- coding: utf-8 -*-
import telebot

help_str = 'привет, я бот, меня создал Сергей.'
token = '440806168:AAFUJqb3TBBCUud87tvRSvsF_FVjnysX-mA'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help',])
def handle_start_help(message):
    bot.send_message(message.chat.id,help_str)
    pass

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)
    print(message.text,' ',message.chat.id)

if __name__ == '__main__':
     bot.polling(none_stop=True)
