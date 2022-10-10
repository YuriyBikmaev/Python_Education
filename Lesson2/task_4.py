# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

number = 3
result = 1
lst = list(range(-number, number+1))
print(lst)
data = open('file.txt', 'r')
for el in data.readlines():
    result *= lst[int(el)-1]
print(result)
