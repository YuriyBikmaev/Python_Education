# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
# Пример
# 6782 -> 23
# 0.56 -> 11

# первый вариант
def SumElementNumberInString(str_number):
    result = 0
    for i in range(len(str_number)):
        result += int(str_number[i])
    return result


number = float(input('Введите вещественное число: '))
print(SumElementNumberInString(''.join(str(number).split('.'))))

# второй вариант
print(sum(map(int, ''.join(str(number).split('.')))))
