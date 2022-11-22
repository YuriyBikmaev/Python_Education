# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
# Пример
# 6782 -> 23
# 0.56 -> 11

while True:
    number = input('Введите вещественное число: ').replace(',', '.')
    try:
        if float(number):
            break
    except:
        print('Введите корретное вещественное число')
print(sum(map(int, filter(lambda el: el.isdigit(), list(number)))))
