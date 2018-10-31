import requests
import re
import config


class HomeTask:
    def __init__(self, userid):
        self.userid = userid
        self.userlogin = config.look(userid)[0]
        self.userpassword = config.look(userid)[1]

    def get_hometask_for_the_day(self, day):
        session = requests.Session()
        page = session.post('https://hselyceum.eljur.ru', {
            'username': self.userlogin,
            'password': self.userpassword,
            'remember': 1,
        })
        page = session.post('https://hselyceum.eljur.ru/journal-app/u.21066/week.1').text
        day_of_the_week = (('Понедельник', 0), ('Вторник', 1), ('Среда', 2), ('Четверг', 3), ('Пятница', 4), ('Суббота', 5))
        content = page.split('width="205px">')[1::]
        hometask = ''
        for days in day_of_the_week:
            if days[0] == day:
                area = content[days[1]]
                subs = area.split('<h4>')[1::]
                for sub in subs:
                    if '<div class="diary__day__lesson__hometask">' in sub:
                        task = sub.split('<div class="diary__day__lesson__hometask">')[1].split('</div>')[0]
                    else:
                        task = 'нет домашнего задания'
                    chars_for_replace = ['&nbsp;', '&quot;', '	&ensp;', '	&ensp;', '	&ensp;', '	&ensp;', '&shy;' '\t', '\n', '\v']
                    task = ''.join(c for c in task if c not in chars_for_replace)
                    task = task.strip()
                    subject = sub.split('</h4>')[0]
                    hometask += subject + '\n' + task + '\n\n'
                print(hometask)

if __name__ == "__main__":
    NastyaJessy = HomeTask('test')
    NastyaJessy.get_hometask_for_the_day('Вторник')