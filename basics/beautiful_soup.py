import requests
from bs4 import BeautifulSoup

#act_nr = input()
#pygmalion_link = input()
#
#r=requests.get(pygmalion_link)
#soup = BeautifulSoup(r.content, 'html.parser')
#
#all_links = soup.find_all('a')
#print(all_links[int(act_nr)-1].get('href'))

article = input()

r=requests.get(article)
soup = BeautifulSoup(r.content, 'html.parser')

print(soup.h1.text)

