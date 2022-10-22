# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

from polynomial import *


def parser_polynomial(str_pol):
    lst = str_pol[:-4].split(' + ')
    lst = [lst[i].replace('^', '').replace('*', '') for i in range(len(lst))]
    lst = lst[::-1]
    for i in range(len(lst)):
        if is_number(lst[i]):
            lst[i] = [lst[i], '0']
        elif lst[i] == 'x':
            lst[i] = ['1', '1']
        elif lst[i][-1] == 'x':
            lst[i] = [lst[i].split('x')[0], '1']
        elif lst[i][0] == 'x':
            lst[i] = ['1', lst[i].split('x')[1]]
        else:
            lst[i] = lst[i].split('x')
    for i in range(int(lst[-1][1])):
        if str(i) < lst[i][1]:
            lst.insert(i, ['0', f'{i}'])
    return [lst[i][0] for i in range(len(lst))]


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


k1 = read_file_polynomial('polynomial_1.txt')
k2 = read_file_polynomial('polynomial_2.txt')
print(k1)
print(k2)
sum_pol = create_polynomial(sum_polynomial(
    parser_polynomial(k1), parser_polynomial(k2)))
print(sum_pol)
write_polynomial_in_file('sum_polynomial.txt', sum_pol)


# print(is_number(parser_polynomial(list_polynomial[1])[0]))
# k_1 = polynomial_1[0][-1]
# k_2 = polynomial_1[0][-1]
# if k_1>len()
