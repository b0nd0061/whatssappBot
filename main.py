import time
import requests
from bs4 import BeautifulSoup as BS
import random
from twilio.rest import Client

def get_love():
    page = str(random.randrange(1,42))
    request = requests.get(f'http://kompli.me/komplimenty-devushke/page/{page}')
    soup = BS(request.text,'lxml').find_all('a')
    lst = []
    for i in soup:
        lst.append(i.text)
    new_lst = lst[4:29]
    return random.choice(new_lst)


def msg_mom_and_dad(event=None, context=None):
    account_sid = 'ACcaee967b6b21ecaf3216479b1be0a664'
    auth_token = 'db7264bc527fefca0ecfff5e7782e91e'
    client = Client(account_sid, auth_token)
    names = ['Василек','Василечек','Васек','Василий Дмитриевич']
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=f'{random.choice(names)} передает: {get_love()}',
        to='whatsapp:+79000492627'
    )
while True:
    time.sleep(3600)
    msg_mom_and_dad()









