# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
# Пример
# 6782 -> 23
# 0.56 -> 11

def SumElementNumber(number):
    result = 0
    while number%10>0:
        result += number%10
        number/=10
    return result

number = float(input('Введите вещественное число: '))
number_1, number_2 = str(number).split('.')
print(SumElementNumber(int(number_1)))

