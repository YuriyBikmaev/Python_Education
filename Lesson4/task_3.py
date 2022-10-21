# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint


def find_unique_element(lst, dictionary=dict()):
    for el in lst:
        if el in dictionary:
            dictionary[el] += 1
        else:
            dictionary[el] = 1
    return [el for el in dictionary if dictionary[el] == 1]


size_list = 10
min_el = 0
max_el = 7
source_list = [randint(min_el, max_el) for _ in range(size_list)]
print(f'Исходный список:\n{source_list}')

print(f'Решение через функцию:\n{find_unique_element(source_list)}')


result_list = [el for el in source_list if source_list.count(el) == 1]
print(f'Решение без функции:\n{result_list}')
