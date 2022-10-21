# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
from unittest import result


# def generate_expr(k):
#     result = ''
#     while k > 0:
#         rand = randint(0, 100)
#         if k == 1:
#             k_op = 'x'
#         else:
#             k_op = f'x^{k}'
#         if rand > 1:
#             result += f'{rand}*{k_op} + '
#         elif rand == 1:
#             result += f'{k_op} + '
#         k -= 1
#     return result + f'{randint(0, 100)} = 0'


def create_polynomial(k):
    result = ''
    ratio_list = [randint(0,100) for _ in range(k)]+[randint(1,100)]
    print(ratio_list)
    for i in range(k+1):
        
    return result


# power = int(input("Введите степень: "))
# # with open('task4.txt', 'w', encoding='utf-8') as data:
# #     data.write(res)
# print(create_polynomial(power))

from random import randint
max_val=100
k = int(input('Введите натуральную степень k:'))
# коэфф. при старшей степени не должен быть равен 0
koeff=[randint(0,max_val) for i in range(k)]+[randint(1,max_val)]
poly='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(koeff) if j][::-1])
# Поиск и замены:
poly=poly.replace('x^1+', 'x+')
poly=poly.replace('x^0', '')
poly+=('','1')[poly[-1]=='+']
poly=(poly, poly[:-2])[poly[-2:]=='^1']
print(poly)