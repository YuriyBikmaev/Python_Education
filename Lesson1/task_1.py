# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

number_day = int(input('Введите день недели: '))
print('да' if (5 < number_day < 8) else 'нет')