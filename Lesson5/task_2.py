# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import choice


def step_game(count, start_player, list_player, block):
    count -= take_candy(list_player[start_player], block)
    start_player == 0 if start_player==1 else 1
    print(f"Осталось\n{count}")


def take_candy(name, block):
    try:
        while True:
            res = int(input(f"Игрок_{name} возьмет конфет:"))
            if res<=block and res>=0:
                return res
            else:
                print(f'{name}, Вы можете взять не больше {block} конфет')
    except:
        print('Введите колличество конфет')


candy = 101
block_take = 28
print('На столе лежит 2021 конфета.' +
      '\n Играют два игрока делая ход друг после друга.'
      '\n Первый ход определяется жеребьёвкой.'
      '\n За один ход можно забрать не более чем 28 конфет.'
      '\n Все конфеты оппонента достаются сделавшему последний ход.')
starting_player = choice([0, 1])
players = [input(f'Введите имя {i+1} игрока:\n') for i in range(2)]
print(f'Игру начинает {players[starting_player]}')
while True:
    step_game(candy, starting_player, players, block_take)
    if candy==0:
        print('Игра окончена')
        break
        
#     take = take_candy(player[0])
#     candy -= take
#     progress[0] += take
#     step_game(candy)
#     take = take_candy(player[1])
#     candy -= take
#     progress[1] += take
#     step_game(candy)
#     if candy == 0:
#         break
