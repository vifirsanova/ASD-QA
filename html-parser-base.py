# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.link')

soup = BeautifulSoup(r.content, features="html.parser")
posts = soup.findAll('li', attrs={'class': 'class'})
