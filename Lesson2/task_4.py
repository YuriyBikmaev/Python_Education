# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

number_n = 3
result = 1
lst = list(range(-number_n, number_n+1))
print(lst)
data = open('file.txt', 'r')
for el in data:
    result *= lst[int(el)-1]
print(result)
