# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности. Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]




source = [1, 2, 3, 5, 1, 5, 3, 10]
result = {}
for el in source:
    if result.get(el):
        result[el] += 1
    else:
        result[el] = 1

print([el for el in result if result[el] == 1])
print([el for el in result if result[el] > 1])
print([el for el in result])

print([*filter(lambda el: result[el]==1, result)])
print([*filter(lambda el: result[el]>1, result)])
print([*filter(lambda el: el, result)])