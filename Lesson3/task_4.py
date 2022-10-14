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


def checking_input_decimal():
    while True:
        input_data = input('Введите десятичное число: ')
        if not input_data.isdecimal():
            print(f'{input_data} не является десятичным числом')
        else:
            return int(input_data)


number = checking_input_decimal()
print(f'{number} -> ' + convert_decimal_to_bin(number))
