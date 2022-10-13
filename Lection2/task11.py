# Напишите программу, которая принимает на вход число N и выдает последовательность из N членов
# для N=5 1, -3, 9, -27, 81

number = int(input("Введите число: "))
for i in range(number):
    print((-3)**i, end = " ")
print()
print(*[(-3)**i for i in range(number)])