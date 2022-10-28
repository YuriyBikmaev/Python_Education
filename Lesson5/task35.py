# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.


with open('Lesson5\import.txt', 'r', encoding = 'utf8') as data:
    a = list(map(int, data.readline().split()))

print(a)
# res = [a[i]-1 for i in range(1,len(a)) if a[i]-1 != a[i-1]]
index = list(filter(lambda i: a[i]-1 != a[i-1], range(1, len(a))))[0]
print(a[index]-1)
# for i in range(len(a)):
#     if a[i]-1 != a[i-1]:
#         print(a[i]-1)
