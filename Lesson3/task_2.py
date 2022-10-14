# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def multiplication_pairs_number(lst):
    size_lst = len(lst)
    middle_size = size_lst//2
    if size_lst % 2 > 0:
        middle_size += 1
    result = [lst[i]*lst[-(i+1)] for i in range(middle_size)]
    return result


source_list = [2, 3, 4, 5, 6]
print(f'Исходный список:\n{source_list}')
print(f'Результат:\n{multiplication_pairs_number(source_list)}')
