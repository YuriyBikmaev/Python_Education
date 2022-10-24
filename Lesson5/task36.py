# Дан список чисел. Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7]

def cmp(x,y):
    if y>x:
        return y
    else:
        return x


source_list = [1, 5, 2, 3, 4, 6, 1, 7]
prev = source_list[:1]
for i in range(1, len(source_list)):
    if source_list[i]>prev[-1]:
        prev.append(source_list[i])    
print(prev)