#!/usr/bin/env python
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup 

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)

def get_doubles_partner(str):
    word_list = str.split(' ')
    if len(word_list) > 3:
        return word_list[-2] + ' ' + word_list[-1]
    return ''

def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

def get_goods(url, csvfile):
    html = BeautifulSoup(simple_get(url), 'html.parser')
    awayt = []
    homet = []
    for i in html.find_all('div', class_ = 'game_summary nohover'):
        count = 0
        for j in i.find_all('tr', class_ = ['loser', 'winner']):
            a = j.find_all('td')
            if (count % 2 == 0):
                awayt.append(append_array(a))
            else:
                homet.append(append_array(a))
            count += 1
    for a, b in zip(awayt, homet):
        if (a == 'D2' or b == 'D2'):
            continue
        else:
            csvfile.write(f'{a}, {b}\n')

def append_array(a):
    if (a[0].find('a').has_attr('href')):
        return a[0].find('a').get_text() + ', ' + a[1].get_text()
    else:
        return 'D2'