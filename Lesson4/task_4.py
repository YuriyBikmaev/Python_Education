# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
from polynomial import create_polynomial
from polynomial import write_polynomial_in_file


k = 2
ratio_lst = ratio_list = [randint(0, 100) for _ in range(k)]+[randint(1, 100)]
polynom = create_polynomial(ratio_lst)
print(polynom)
write_polynomial_in_file('polynomial_1.txt', polynom)
