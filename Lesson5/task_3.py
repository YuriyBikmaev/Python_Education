# Создайте программу для игры в ""Крестики-нолики"".

from random import choice


def check_win(field, symbol):
    size = int(len(field)**0.5)
    matrix = [field[i:i+size] for i in range(0, len(field), size)]
    res = [''.join(matrix[i]) for i in range(0, size)]
    res += [''.join(field[i::size]) for i in range(size)]
    res += [''.join([matrix[i][i] for i in range(size)])]
    res += [''.join([matrix[i][size-1-i] for i in range(size)])]
    if symbol*size in res:
        return True
    return False


def print_field(field):
    s = int(len(field)**0.5)
    for i in range(s):
        print_str = ''
        for j in range(s):
            print_str += ':'.ljust(3) + str(field[i*s+j]).ljust(3)
        print_str += ':'.ljust(3)
        if i == 0:
            print('-'*(len(print_str)-2))
        print(print_str)
        print('-'*(len(print_str)-2))


def choise_pos(player, field, c):
    while True:
        try:
            pos = int(input(f'{player}, введите номер поля: '))
            if field[pos-1] != 'X' or field[pos-1] != 'O':
                field[pos-1] = c
                break
            else:
                print('Указаное поле занято!')
        except:
            print('Введите корретный номер поля')


def step_game(start_player, dict_player, st, field):
    win_player = ''
    if st % 2 == 0:
        choise_pos(dict_player[start_player], field, 'X')
        if check_win(field, 'X'):
            win_player = dict_player[start_player]
    else:
        choise_pos(dict_player[1 if start_player == 0 else 0], field, 'O')
        if check_win(field, 'O'):
            win_player = dict_player[1 if start_player == 0 else 0]
    print_field(field)
    if win_player == '':
        while st < len(field)-1:
            st += 1
            return step_game(start_player, dict_player, st, field)
        if st == len(field):
            print('Ничья!')
    else:
        print('Победитель - '+win_player+'!')

print("Добро пожалось в игру КРЕСТИКИ-НОЛИКИ")
starting_player = choice([0, 1])
players = [input(f'Введите имя {i+1} игрока:\n') for i in range(2)]
print(f'Игру начинает {players[starting_player]}')
size_field = 3
playing_field = [str(i) for i in range(1, size_field**2+1)]
print_field(playing_field)
step_game(starting_player, players, 0, playing_field)
