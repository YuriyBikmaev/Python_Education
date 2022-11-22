import json
import requests
from bs4 import BeautifulSoup
import datetime


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

def fill_block_city(path_file):
    data = open(path_file, 'r', encoding='utf8')
    result = [el[:-1] for el in data]
    data.close()
    return result


def fill_arrival_board(path_site, block_board):
    current_year = datetime.datetime.today().year
    kuf = requests.get(path_site)
    if str(kuf)[-5:-2] == '200':
        kufaero = BeautifulSoup(kuf.content, "html.parser")
        kuf_table = kufaero.find_all(class_="table-flex__row")
        result = []
        for board in kuf_table:
            middle_res = ''
            arrival_board = board.find(
                class_="table-flex__td table-flex__td--type2")
            if arrival_board:
                middle_res += str(arrival_board).split()[
                    3][6:].split('<')[0] + ' '
            date = board.find(class_="table-flex__td table-flex__td--type6")
            if date:
                middle_res += date.find(
                    class_="board__text-extra").string.strip() + f'.{current_year} '
                middle_res += date.find(class_="board__text").string.strip() + ' '
            where_board = board.find(
                class_="table-flex__td table-flex__td--type4")
            if where_board:
                middle_res += where_board.find(
                    class_="board__text-extra").string.strip() + ' '
                middle_res += where_board.find(
                    class_="board__text").string.strip() + ' '
            status_board = board.find(
                class_="table-flex__td table-flex__td--type5")
            if status_board:
                if status_board.find(class_="color-"):
                    middle_res += status_board.find(
                        class_="color-").string.strip()
                else:
                    middle_res += status_board.find(
                        class_="color-green").string.strip()
            if middle_res != '':
                lst_aero = middle_res.split()
                if len(lst_aero) == 7:
                    lst_aero = lst_aero[:4] + [lst_aero[4] +
                                               ' '+lst_aero[5]] + lst_aero[-1:]
                if lst_aero[4] not in block_board:
                    result.append(lst_aero)
        return result


board_block = fill_block_city('Parser\city.txt')
arrival = fill_arrival_board(
    "https://kuf.aero/board/?type=arr&date=yesterday", board_block)
arrival += fill_arrival_board(
    "https://kuf.aero/board/?type=arr&ready=yes", board_block)
arrival += fill_arrival_board(
    "https://kuf.aero/board/?type=arr&date=tomorrow", board_block)
[print(el) for el in arrival]
