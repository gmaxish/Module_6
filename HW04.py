"""
Дан диапазон целых чисел от N1 до N2. Найдите факториал каждого третьего простого числа в заданном диапазоне.
"""
primes = []


def fact(t):
    a, b = 0, 1
    while a < t:
        print(a)
        a, b = b, a+b


def isPrime(t):
    for j in range(2, t//2+1):
        if t % j == 0:
            return False
    else:
        primes.append(t)
        return True

N1 = 1
N2 = 22

for i in range(N1, N2+1):
    isPrime(i)
print(primes)
for i in primes[2::3]:
    print(" i:", i)
    fact(i)
