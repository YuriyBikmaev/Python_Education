# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def CheckQuarter(quarter):
    match quarter:
        case 1: print('(x>0, y>0)')
        case 2: print('(x<0, y>0)')
        case 3: print('(x<0, y<0)')
        case 4: print('(x>0, y<0)')
        case _: print(f'{quarter} четверти не существует')


number_quarter = int(input('Введите номер четверти системы координат: '))
CheckQuarter(number_quarter)
