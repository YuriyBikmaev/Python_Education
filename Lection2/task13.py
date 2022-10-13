# Напишите программу в которой пользователь будет задавать две строки, а программа определять колимчество вхождений одной строки в другой
# "hello or world", "or" -> 2

def FindStr(str1, str2):
    count = 0
    size = len(str2)
    for i in range(len(str1)-size+1):
        if str1[i:i+size] == str2:
            count += 1
    return count


str_1 = "abababa"
str_2 = "aba"


print(FindStr(str_1, str_2))
