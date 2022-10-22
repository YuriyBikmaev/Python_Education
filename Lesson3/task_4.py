# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def convert_decimal_to_bin(n, result=''):
    if n > 0:
        while n/10 > 0:
            result = str(n % 2) + result
            n //= 2
    else:
        result = '0'
    return result


def rec_bin(n):
    if n <= 0:
        return 0
    else:
        return n%2 + 10*rec_bin(n//2)


def checking_input_decimal():
    while True:
        input_data = input('Введите десятичное число: ')
        if input_data.isdecimal():
            return int(input_data)
        else:
            print(f'{input_data} не является десятичным числом')


number = checking_input_decimal()
print(f'{number} -> {rec_bin(number)}')
