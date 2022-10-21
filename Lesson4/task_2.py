# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def sieve_prime_numbers(n):
    sieve = [True] * n
    # в цикле начинаем с 3 и пропускаем все четные числа
    for i in range(3, int(n**0.5)+1, 2):
        # отсеиваем числа кратные i
        if sieve[i]:
            sieve[i*i::2*i] = [False] * len(sieve[i*i::2*i])
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def find_multiplier(n):
    prime_numbers = sieve_prime_numbers(n)
    return [i for i in prime_numbers if n % i == 0]


n = 1241
print(find_multiplier(n))
