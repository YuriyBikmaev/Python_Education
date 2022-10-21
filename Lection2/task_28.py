# Найдите корни квадратного уравнения Ax² + Bx + C = 0, где A ≠ 0 двумя способами: 1) с помощью математических формул нахождения корней квадратного уравнения 2) с помощью дополнительных библиотек Python

# test_data = [
#     [[1, -3, 2], [1.0, 2.0]],
#     [[1, 2, 1], [-1, -1]],
#     [[2, 2, 1], []]
# ]

# for nums, expected in test_data:
#     assert quadratic_equation(*nums) == expected

def quadratic_equation(lst):
    discremenant = lst[1]**2 - 4*lst[0]*lst[2]
    if discremenant < 0:
        print ("Корней нет")
        return []
    elif discremenant > 0:
        x1 = -((lst[1]+discremenant**0.5)/(2*lst[0]))
        x2 = -((lst[1]-discremenant**0.5)/(2*lst[0]))
        return [x1, x2]
    else:
        x1 = (-lst[1]/(2*lst[0]))
        return [x1]
    

print(quadratic_equation([1, -3, 2]))
