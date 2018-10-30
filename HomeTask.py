import requests
import re
import config

def rplc(st):
    chars = ['[', '\'', ',', ']', '<h4>', '\'']
    for char in chars:
        st = st.replace(char, '')
    return st

def HomeTask(userid):
    session = requests.Session()
    username = str(config.authen[userid]).split(' ')
    usr = rplc(username[0])
    pas = rplc(username[1])
    page = session.post('https://hselyceum.eljur.ru', {
        'username': usr,
        'password': pas,
        'remember': 1,
    })
    page = session.post('https://hselyceum.eljur.ru/journal-app/view.journal').text
    Day_of_the_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
    day = 'Вторник'
    if (day == 'Понедельник'):
        rez = day + "\n" + '\n'
        area = (page.split('<td  width="205px">Понедельник'))[1]
        area = (area.split('<td  width="205px">Вторник'))[0]
        area = area.split('<h4>')
        area = area[1::]
        for sub in area:
            rez += sub.split('</h4>')[0] + '\n'
            if '<div class="diary__day__lesson__hometask">' in sub:
                hometask = (sub.split('<div class="diary__day__lesson__hometask">'))[1]
                hometask = (hometask.split('</div>'))[0]
                rez += hometask.strip() + '\n'
            else:
                rez += "нет домашнего задания" + '\n'
            rez += '\n'

    if (day == 'Вторник'):
        rez = day + "\n" + '\n'
        area = (page.split('<td  width="205px">Вторник'))[1]
        area = (area.split('<td  width="205px">Среда'))[0]
        area = area.split('<h4>')
        area = area[1::]
        for sub in area:
            rez += sub.split('</h4>')[0] + '\n'
            if '<div class="diary__day__lesson__hometask">' in sub:
                hometask = (sub.split('<div class="diary__day__lesson__hometask">'))[1]
                hometask = (hometask.split('</div>'))[0]
                rez += hometask.strip() + '\n'
            else:
                rez += "нет домашнего задания" + '\n'
            rez += '\n'
    return rez
