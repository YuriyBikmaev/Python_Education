# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def find_multiplier(n):
    result = []
    if n>9:
        while n%2==0:
            result.append(2)
            n/=2
        while n%3==0:
            result.append(3)
            n/=3
    if n<10:
        result.append(int(n))
    
    return result

print(find_multiplier(84))
         
