import requests

session = requests.Session()
page = session.post('https://hselyceum.eljur.ru', {
    'username': '1',
    'password': '1',
    'remember': 1,
})
page = session.post('https://hselyceum.eljur.ru/journal-app/view.journal')