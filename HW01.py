"""
Дана последовательность целых чисел. Для каждого числа последовательности найти количество его делителей.
"""

l = [3, 5, 2, 12, 6, 7, 14, 70]
deliteli = []


def delit(n):
    for k in range(1, i+1):
        if i % k == 0:
            #print(k, "delitel", i)
            deliteli.append(k)
    print("Для числа", i, "количество делителей", len(deliteli))
    deliteli.clear()


for i in l:
    delit(i)
