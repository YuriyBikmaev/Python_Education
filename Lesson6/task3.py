# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def multiplication_pairs_number(lst):
    return [lst[i]*lst[-(i+1)] for i in range((len(lst)+1)//2)]


source_list = [2, 3, 4, 5, 6]
print(f'Исходный список:\n{source_list}')
print(f'Результат:\n{multiplication_pairs_number(source_list)}')
