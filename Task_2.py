# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
n = int(input('Введите простое число: '))

def fact_prime_num(n):
    p = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            p.append(d)
            n //= d
        d += 1
    if n > 1:
        p.append(n)
    return p

print(fact_prime_num(n))

