# Создайте программу для игры в ""Крестики-нолики"".

# tic_tac_toe

from random import randint


def choise_pos(player, field, c):
    while True:
        pos = int(input(f'{player}, введите номер поля: '))
        if field[pos-1][1]:
            field[pos-1] = [c, False]
            break
        else:
            print('Указаное поле занято!')


def check_win(field):
    # res = list(zip(field[0:3], field[3:6], field[6:9]))
    # print res
    ...


def print_field(field):
    count = 0
    for i in range(7):
        if i % 2 == 0:
            print('-'*13)
        else:
            print('| ' + str(field[count][0]) + ' | ' +
                  str(field[count+1][0]) + ' | ' + str(field[count+2][0]) + ' |')
            count += 3


def step_game(start_player, dict_player, st, field):
    if st % 2 != 0:
        choise_pos(dict_player[start_player], field, 'X')
    else:
        choise_pos(dict_player[1 if start_player == 0 else 0], field, '0')
    print_field(field)


step = 0
#starting_player = randint(0, 1)
# players = [(input(f'Введите имя {i+1} игрока:\n'), '') for i in range(2)]
starting_player = 0
players_name = ['Анатолий', 'Вера']
players = {0: players_name[0], 1: players_name[1]}
print(f'Игру начинает {players[starting_player]}')

playing_field = [[str(i), True] for i in range(1, 10)]
print(playing_field)

# https://habr.com/ru/post/329300/ про алгоритм проверки результата игры

print(progress)
print((progress[0]))

while step<9:
    step += 1
    print(progress)
    step_game(starting_player, players, step, playing_field)
