# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fibo(n): 
    if n == 0:
        return 0
    elif n == 1 or n == -1:
        return 1
    elif n < -1:
        return int((-1)**(n+1)*(fibo(-n-2)+fibo(-n-1)))
    else:
        return (fibo(n-2)+fibo(n-1))


def generate_fib_list(n, ):
    result = []
    for i in range(-n, n+1):
        result.append(fibo(i))
    return result


print(generate_fib_list(8))

# def generate_fib_list(n):
#     result = []
#     for i in range(n+1):
#         if i == 0:
#             result.append(i)
#         elif i == 1:
#             result.append(i)
#             result.insert(0, i)
#         else:
#             fn = result[-2] + result[-1]
#             result.append(fn)
#             result.insert(0, ((-1)**(i+1))*fn)
#     return result


# k = 8
# print(generate_fib_list(k))
