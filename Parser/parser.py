import json
import requests
from bs4 import BeautifulSoup


# datafile = open('Python_Education\Parser\webinars.json', 'r', encoding='utf-8')
# data = json.load(datafile)
# #[webinar["speaker"] for webinar in data]
# #print([webinar["speaker"] for webinar in data])
# datafile.close


# htmlfile= open('Python_Education\Parser\skillbox.html', 'r', encoding='utf-8')
# code = htmlfile.read()
# soup = BeautifulSoup(code, "html.parser")
# links = soup.findAll('a')
# #print(*[link.string.strip() for link in links]) #вывод меню
# print(*[link['href'] for link in links]) #вывод ссылок

kuf = requests.get("https://kuf.aero/board/?type=arr")
print(kuf)
#board__text-extra

kufaero = BeautifulSoup(kuf.content, "html.parser")
kuf_table = kufaero.find_all(class_ = "table-flex__row")
result = []
for board in kuf_table:
    middle_res = ''
    arrival_board = board.find(class_ = "table-flex__td table-flex__td--type2")
    if arrival_board:
       middle_res += str(arrival_board).split()[3][6:].split('<')[0] + ' '
        # print(arrival_board.attrs['table-flex__td'])
        # middle_res += str(arrival_board) + ' '
    date = board.find(class_ = "table-flex__td table-flex__td--type6") 
    if date:
        middle_res += date.find(class_ = "board__text-extra").string.strip() + ' '
        middle_res += date.find(class_ = "board__text").string.strip() + ' '
    where_board = board.find(class_ = "table-flex__td table-flex__td--type4")
    if where_board:
        middle_res += where_board.find(class_ = "board__text-extra").string.strip() + ' '
        middle_res += where_board.find(class_ = "board__text").string.strip() + ' '
    status_board = board.find(class_ = "table-flex__td table-flex__td--type5")
    if status_board:
        middle_res += where_board.find(class_ = "board__text-extra").string.strip()
    if middle_res != '':
        result.append(middle_res.split())
    
print(result)
