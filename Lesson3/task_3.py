# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from decimal import *


def difference_fraction_max_min(lst, accuracy, max=0, min=1):
    getcontext().prec = accuracy
    for el in lst:
        if isinstance(el, float):
            fraction = Decimal(el) % 1
            if fraction < 0:
                fraction += 1
            if max < fraction:
                max = fraction
            if min > fraction:
                min = fraction
    if min == 1:
        min = 0
    return float(max-min)


source_list = [1.1, 1.2, 3.1, 5, 10.01]
print(f'Исходный список:\n{source_list}')
print(f'Результат: {difference_fraction_max_min(source_list, 4)}')
