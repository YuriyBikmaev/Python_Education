# Напишите программу, которая принимает на фход число N и выдает набор произведений чисел от 1 до N
# Пример
# N=4, [1,2,6,24] ()


number = int(input('Введите число N: '))
result = []
for i in range(1, number+1):
    if i > 1:
        result.append(i*result[i-2])
    else:
        result.append(i)
print(result)
