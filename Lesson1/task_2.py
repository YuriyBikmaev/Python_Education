# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def CheckTruth(x, y, z):
    return ((not (x or y or z)) == (not x and not y and not z))


number_x = input("Введите значение x: ")
number_y = input("Введите значение y: ")
number_z = input("Введите значение z: ")
print(CheckTruth(number_x, number_y, number_z))
