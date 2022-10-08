# Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).

quarter = int(input('Введите номер четверти системы координат: '))
if quarter == 1:
    print('(x>0, y>0)')
elif quarter == 2:
    print('(x<0, y>0)')
elif quarter == 3:
    print('(x<0, y<0)')
elif quarter == 4:
    print('(x>0, y<0)')
else:
    print(f'{number_quarter} четверти не существует')
