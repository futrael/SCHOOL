import config
import telebot
from telebot import types
import requests
import re
import config
from TimeTable import TimeTable

bot = telebot.TeleBot(config.token)



@bot.message_handler(regexp="Расписание")
def timetable_choose(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('расписание на день')
    markup.row('расписание на неделю')
    bot.send_message(message.chat.id, reply_markup=markup)
    bot.register_next_step_handler(message, timetable)

def timetable(message):
    if message.text == 'расписание на день':
        pass
    if message.text == 'расписание на неделю':
        print(TimeTable(message.chat.id).get_timetable_for_the_week())



@bot.message_handler(regexp="/start")
def start(message):
    bot.send_message(message.chat.id, "Введите свой логин и пароль от элжура через пробел")
    bot.register_next_step_handler(message, register)


def register(message):
    usr = str(message.text).split(' ')
    config.load({str(message.chat.id): [usr[0], usr[1]]})
    print(config.watch())
    if not check_register(message.chat.id):
        markup = types.ReplyKeyboardMarkup()
        markup.row('Оценки', 'Расписание', 'Домашнее задание', 'Сменить аккаунт')
        bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Неверный логин или пароль")
        bot.send_message(message.chat.id, "Введите свой логин и пароль от элжура через пробел")
        bot.register_next_step_handler(message, register)


def check_register(userid):
    session = requests.Session()
    userpage = session.post('https://hselyceum.eljur.ru', {
        'username': config.look(userid)[0],
        'password': config.look(userid)[1],
        'remember': 1,
    })
    return '{"uid":null,"username":null,"role":null,"domain":"hselyceum"}' in userpage.text


if __name__ == '__main__':
    bot.polling(none_stop=True)
