import requests
import re
import config

# -*- coding: utf-8 -*-

TimetableLink = 'https://hselyceum.eljur.ru/journal-app/week.-2'


# регулярка для нахождения дней недели <p class="schedule__day__content__header__date">[0-9]*.[0-9]*</p>                        <p>[А-Яа-я]*</p>

def rplc(st):
    chars = ['[', '\'', ',', ']', '<h4>', '\'']
    for char in chars:
        st = st.replace(char, '')
    return st


def Ttable(userid):
    session = requests.Session()
    username = str(config.authen[userid]).split(' ')
    usr = rplc(username[0])
    pas = rplc(username[1])
    page = session.post('https://hselyceum.eljur.ru', {
        'username': usr,
        'password': pas,
        'remember': 1,
    })
    page = str(session.post(TimetableLink).text)
    page = page.split('<td  width="2')
    rez = ''
    for days in page:
        day = str(re.findall('05px">[А-Яа-я]+', str(days)))
        day = (re.findall('[А-Яа-я ]+', day))
        lessons = rplc(str(re.findall('<h4>[^\d]+</h4>', str(days))))
        lessons = lessons.split('</h4>')
        rez += str(*day) + '\n'
        i = 1
        for lesson in lessons:
            if i == 1:
                rez += ' ' + str(lesson) + '\n'
            else:
                rez += str(lesson) + '\n'
            i += 1
        rez += '\n'
    return rez
