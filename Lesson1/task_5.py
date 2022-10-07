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


def CalculateLengthSegment(a, b):
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5


coordinate_A = InputCoordinateXY('A')
coordinate_B = InputCoordinateXY('B')
print(
    f'Расстояние между точками А{coordinate_A} и B{coordinate_B} = {CalculateLengthSegment(coordinate_A, coordinate_B):.2f}')
