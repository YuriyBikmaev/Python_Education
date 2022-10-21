# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from cmath import pi
from decimal import *


def calc_pi_v2(accuracy):
    k = Decimal(1)
    dec = Decimal(12**0.5)
    s1 = Decimal(0)
    s2 = Decimal(0)
    i = Decimal(0)
    while True:
        s1 = s2+dec/(k*(3**i))
        i += 1
        k += 2
        s2 = s1-dec/(k*(3**i))
        i += 1
        k += 2
        if s1-s2 < accuracy:
            return (s1+s2)/2


getcontext().prec = 16
getcontext().rounding = ROUND_DOWN

print(f'Значение константы:\n{pi}')
d = 0.001
print('Результат:')
print(calc_pi_v2(d).quantize(Decimal(
    f'{1+d}')) if 0.1 >= d >= 0.0000000001 else 'Используйте другую точность')
