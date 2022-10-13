# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
# Пример
# 6782 -> 23
# 0.56 -> 11

from decimal import *

getcontext().prec = 10
sum = 0
num = 12.3456
num_whole = num//1
num_fr = Decimal(num)%Decimal(1)

while num_fr%1 > 0:
     num_fr *=10
     sum += int(num_fr%10)

while num_whole%10 > 0:
    sum += int(num_whole%10)
    num_whole //= 10
print(sum)
