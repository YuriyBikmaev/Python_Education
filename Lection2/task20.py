# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# Пример:
# ["qwe", "asd", "12", "qwe", "2"], 2 -> True
# ["qwe", "asd", "qwe", "681"], 7 -> False
# ["qwe", "asd", "qwe", "0"], 0 -> True

def find(lst, number):
    for el in lst:
        if el==str(number):
            return True
    return False

lst1 = ["qwe", "asd", "3", "qwe", "23"]
str_in = 23
print(find(lst1, str_in))

print(str(str_in) in ''.join(lst1))