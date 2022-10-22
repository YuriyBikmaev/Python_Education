# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


def create_polynomial(power):
    ratio_list = [randint(0,100) for _ in range(power)]+[randint(1,100)]
    result = ''
    print(ratio_list)
    for i,j in enumerate(ratio_list):
        if i==0:
            k = ''
        elif i==1:
            k = 'x'
        else:
            k = f'x^{i}'
        if j>1:
            result = f'{j}*' + k + ' ' + result
        elif j==1:
            result += k + ' ' + result 
    if result[-2]=='*':
        result = result[:-2] + ''
    return ' + '.join(result.split())+' = 0'


k = 2
polynomial = create_polynomial(k)
print(polynomial)
data = open('polynomial_1.txt', 'w', encoding='utf-8')
data.write(polynomial)
data.close
