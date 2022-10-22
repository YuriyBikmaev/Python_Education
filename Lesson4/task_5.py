# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# data = open('polynomial_1.txt', 'r', encoding='utf-8')
# polynomial_1 = data.readline()
# data.close
# data = open('polynomial_2.txt', 'r', encoding='utf-8')
# polynomial_2 = data.readline()
# data.close

from gettext import find


def read_two_polynomial(n):
    polynomial = []
    for i in range(n):
        data = open(f'polynomial_{i+1}.txt', 'r', encoding='utf-8')
        polynomial.append(data.readline()[:-4].split(' + '))
        data.close
    return polynomial

def parser_polynomial(lst):
    result = ()
    
    # for i in range(len(lst)):
    #     lst_el = str(lst[i]).split('*')
    #     if not isinstance(lst_el[0], int):
    #         if lst_el[0] == 'x':
    #             lst[i] == 1
    #         else:
    #             lst[i] == int(lst_el[0])
    # if int(lst[0][-1])+1>len(lst):
    #     result = [0]*(int(lst[0][-1])+1-len(lst))
    return type(result)

list_polynomial = read_two_polynomial(2)
print(list_polynomial)
print(parser_polynomial(list_polynomial[0]))
# k_1 = polynomial_1[0][-1]
# k_2 = polynomial_1[0][-1]
# if k_1>len()
