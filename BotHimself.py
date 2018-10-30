# -*- coding: utf-8 -*-
from telebot.types import User, Chat

import config
import telebot
from telebot import types
import requests
import re

bot = telebot.TeleBot(config.token)


def rplc(st):
    chars = ['[', '\'', ',', ']', '<h4>', '\'']
    for char in chars:
        st = st.replace(char, '')
    return st


def check(userid):
    session = requests.Session()
    username = str(config.authen[userid]).split(' ')
    usr = rplc(username[0])
    pas = rplc(username[1])
    page = session.post('https://hselyceum.eljur.ru', {
        'username': usr,
        'password': pas,
        'remember': 1,
    })
    page = session.post('https://hselyceum.eljur.ru/journal-app/view.journal')
    list_of_subj = \
    (page.text.split('<div id="g0_journal" data-grid-control="columns-body" xls_group="0" xls_list="grp0">'))[1]
    list_of_subj = (list_of_subj.split('<div id="g0_scroller" class="grid-scroll " data-grid-control="scroll-body">'))[
        0]


@bot.message_handler(regexp="/start")
def Srart(message):
    bot.send_message(message.chat.id, "Введите свой логин и пароль от элжура через пробел")
    print(message.text)
    bot.register_next_step_handler(message, Srart)


@bot.message_handler(regexp="Сменить аккаунт")
def Change(message):  # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, "Введите свой логин и пароль от элжура через пробел")
    print(message.text)
    bot.register_next_step_handler(message, Srart)


@bot.message_handler(regexp="Оценки")
def Marks(message):  # Название функции не играет никакой роли, в принципе
    import Marks
    print(message.chat.id)
    try:
        check(str(message.chat.id))
        bot.send_message(message.chat.id, Marks.Mrks(str(message.chat.id)))
    except:
        bot.send_message(message.chat.id, "Неверные данные")
        bot.send_message(message.chat.id, "Введите свой логин и пароль от элжура через пробел")
        bot.register_next_step_handler(message, Srart)


@bot.message_handler(regexp="Расписание")
def Timetable(message):
    import Timetable
    print(message.chat.id)
    try:
        check(str(message.chat.id))
        bot.send_message(message.chat.id, Timetable.Ttable(str(message.chat.id)))
    except:
        bot.send_message(message.chat.id, "Неверные данные")
        bot.send_message(message.chat.id, "Введите свой логин и пароль от элжура через пробел")
        bot.register_next_step_handler(message, Srart)

@bot.message_handler(regexp="Домашнее задание")
def HomeTask(message):
    print(message.chat.id)
    try:
        check(str(message.chat.id))
        markup = types.ReplyKeyboardMarkup()
        markup.row('Понедельник', 'Вторник', 'Среда')
        markup.row('Четверг', 'Пятница', 'Суббота')
        bot.send_message(message.chat.id, "Выберите день:", reply_markup=markup)
    except:
        bot.send_message(message.chat.id, "Неверные данные")
        bot.send_message(message.chat.id, "Введите свой логин и пароль от элжура через пробел")
        bot.register_next_step_handler(message, Srart)

@bot.message_handler(regexp="Вторник")
def Vtornik(message):
    import HomeTask
    print(message.chat.id)
    bot.send_message(message.chat.id, HomeTask.HomeTask(str(message.chat.id)))


def Srart(message):  # Название функции не играет никакой роли, в принципе
    print(message.text)
    usr = str(message.text).split(' ')
    config.authen[str(message.chat.id)] = str(usr)
    print(config.authen)
    try:
        check(str(message.chat.id))
        markup = types.ReplyKeyboardMarkup()
        markup.row('Оценки', 'Расписание', 'Домашнее задание', 'Сменить аккаунт')
        bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)
    except:
        bot.send_message(message.chat.id, "Неверные данные")
        bot.send_message(message.chat.id, "Введите свой логин и пароль от элжура через пробел")
        bot.register_next_step_handler(message, Srart)


if __name__ == '__main__':
    bot.polling(none_stop=True)
