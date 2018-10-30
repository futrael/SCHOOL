import requests
import re
import config


def rplc(st):
    chars = ['[', '\'', ',', ']', '<h4>', '\'']
    for char in chars:
        st = st.replace(char, '')
    return st


def Mrks(userid):
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
    list_of_subj = (page.text.split('<div id="g0_journal" data-grid-control="columns-body" xls_group="0" xls_list="grp0">'))[1]
    list_of_subj = (list_of_subj.split('<div id="g0_scroller" class="grid-scroll " data-grid-control="scroll-body">'))[0]
    list_of_subj = list_of_subj.split('<div class="cell"')
    subj = []
    for sub in list_of_subj:
        sub = re.findall('name="[^\d]*"></div>', sub)
        print(sub)
        sub = str(*sub).replace('name="', '')
        sub = sub.replace('"></div>', '')
        subj.append(sub)
    while ' ' in subj:
        subj.remove(' ')
    result = ''
    for sub in subj:
        mark = str(re.findall('name="' + sub + '"><div class="cell-data">[A-Za-zА-Яа-я0-9]+</div>', str(page.text)))
        mark = str(re.findall('[0-9]', mark))
        chars = "',[]"
        for char in chars:
            mark = mark.replace(char, '')
        result += sub + ' ' + str(mark) + '\n' + '\n'
    return result
