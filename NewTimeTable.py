import requests
import re
import config


class TimeTable:
    def __init__(self, userid):
        self.userid = userid
        self.userlogin = config.look(userid)[0]
        self.userpassword = config.look(userid)[1]
        self.jorid = ''


    def authorization(self):
        session = requests.Session()
        userpage = session.post('https://hselyceum.eljur.ru', {
            'username': self.userlogin,
            'password': self.userpassword,
            'remember': 1,
        })
        time_table_link = 'https://hselyceum.eljur.ru/journal-schedule-action/class.11МИ2/week.both/startdate./forStudent.'
        page = str(session.post(time_table_link).text)
        jorid = str(re.findall('"uid":[0-9]+', page))
        jorid = re.findall('[0-9]+', jorid)[0]
        page = str(session.post(time_table_link + jorid).text)
        return page

    def get_timetable_for_the_day(self, day):
        day_of_the_week = (('Понедельник', 0), ('Вторник', 1), ('Среда', 2), ('Четверг', 3), ('Пятница', 4), ('Суббота', 5))
        page = self.authorization()
        page = page.split('<p class="schedule__day__content__header__date">')[1::]
        for days in day_of_the_week:
            if days[0] == day:
                page = page[days[1]]
                sub = ''
                subjects = re.findall('lesson">[А-Яа-я ]+', page)
                i = 1
                for subj in subjects:
                    sub += str(i) + ') ' + subj.replace('lesson">', '') + '\n'
                    i += 1
                return sub

    def get_timetable_for_the_week(self):
        day_of_the_week = (('Понедельник', 0), ('Вторник', 1), ('Среда', 2), ('Четверг', 3), ('Пятница', 4), ('Суббота', 5))
        rez = ''
        for days in day_of_the_week:
            rez += days[0] + '\n' + self.get_timetable_for_the_day(days[0]) + '\n'
        return rez



if __name__ == "__main__":
    NastyaJessy = TimeTable('test')
    print(NastyaJessy.get_timetable_for_the_week())