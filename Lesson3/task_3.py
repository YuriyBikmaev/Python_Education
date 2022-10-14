# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from decimal import *


def difference_fraction_max_min(lst, accuracy, max=0, min=1):
    getcontext().prec = accuracy
    for el in lst:
        fraction = Decimal(el) % 1
        if max < fraction:
            max = fraction
        if min > fraction:
            min = fraction
    return float(max-min)


source_list = [1.1, 1.2, 3.1, 5.003, 10.01]
print(f'Исходный список:\n{source_list}')
print(f'Результат: {difference_fraction_max_min(source_list, 4)}')
