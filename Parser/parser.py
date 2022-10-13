import json
import requests
from bs4 import BeautifulSoup


datafile = open('Python_Education\Parser\webinars.json', 'r', encoding='utf-8')
data = json.load(datafile)
#[webinar["speaker"] for webinar in data]
#print([webinar["speaker"] for webinar in data])
datafile.close


htmlfile= open('Python_Education\Parser\skillbox.html', 'r', encoding='utf-8')
code = htmlfile.read()
soup = BeautifulSoup(code, "html.parser")
links = soup.findAll('a')
#print(*[link.string.strip() for link in links]) #вывод меню
print(*[link['href'] for link in links]) #вывод ссылок

kuf = requests.get("https://kuf.aero/board/?type=arr")
print(kuf.status_code)
#board__text-extra
kufaero = BeautifulSoup(kuf.content, "html.parser")
kuf_iata = kufaero.findAll('board__text-extra')
print(*kuf_iata)
