# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_elements_odd_position(lst, result=0):
    for i in range(1, len(lst)-1, 2):
        result += lst[i]
    return result


source_list = [2, 3, 5, 9, 3]
print(source_list)
print(
    f'Сумма элементов на нечетных позициях = {sum_elements_odd_position(source_list)}')
