# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

from random import choice, randint
from statistics import mode


def step_game(count, start_player, list_player, block):
    while True:
        count -= take_candy(list_player[start_player], block, count)
        if count <= block:
            block = count
        if count == 0:
            print(f'Игра окончена.\n Победил {list_player[start_player]}!')
            break
        else:
            print(f"Осталось: {count}")
        start_player = 0 if start_player == 1 else 1


def mode_selection():
    print('С кем будете играть?')
    print(' 1. С другим игроком')
    print(' 2. С компьютером')
    try:
        while True:
            res = int(input("Введите номер варианта игры:"))
            if res <= 2 and res >= 1:
                return res
            else:
                print(f'Такого варианта нет!')
    except:
        print('Некорректный ввод!')

def start_game(count_candy, block):
    starting_player = choice([0, 1])
    mode_game = mode_selection()
    if mode_game == 1:
        players = [input(f'Введите имя {i+1} игрока:\n') for i in range(2)]
    else:
        players = [input(f'Введите имя игрока:\n')] + ['Компьютер']     
    print(f'Игру начинает {players[starting_player]}')
    print(f'На столе лежит {count_candy} конфет')
    step_game(count_candy, starting_player, players, block)


def take_intellect(count_candy, block):
    step = int(count_candy//block)
    remains = int(count_candy%block)
    if remains>0:
        step += 1
    if not step%2:
        if count_candy>block*2:
            return remains if remains>0 else block
        else:
            return count_candy-1-block
    else:
        return block
        

def take_candy(name, block, count_candy):
    try:
        while True:
            if name == 'Компьютер':
                res = take_intellect(count_candy, block)
                print(f'Компьютер взял конфет: {res}')
            else:
                res = int(input(f"{name} возьмет конфет:"))
            if res <= block and res >= 0:
                return res
            else:
                print(f'{name}, Вы можете взять не больше {block} конфет')
    except:
        print('Введите колличество конфет')

candy = 2021
block_take = 28
print(f'На столе лежит {candy} конфета.' +
      '\n Играют два игрока делая ход друг после друга.'
      '\n Первый ход определяется жеребьёвкой.'
      '\n За один ход можно забрать не более чем 28 конфет.'
      '\n Все конфеты оппонента достаются сделавшему последний ход.')
start_game(candy, block_take)
