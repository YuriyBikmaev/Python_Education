# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def InputCoordinateXY(name_point):
    result = []
    print('Введите координаты для точки ' + name_point)
    result.append(int(input('x = ')))
    result.append(int(input('y = ')))
    return result


a = InputCoordinateXY('A')
b = InputCoordinateXY('B')
result = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5
print(f'Расстояние между точками А и B = {result:.2f}')
