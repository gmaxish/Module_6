"""
Дана последовательность целых чисел. Для каждого числа последовательности проверить, представляют ли его цифры строго
возрастающую последовательность.
"""
#TODO ?

m = [123, 245, 233, 222, 202, 641, 424, 228]


def tr(t):
    x = [int(a) for a in (str(t))]
    k = 0
    for j in x:
        if j > k:
            k = j
            #print(k)
            return True
        elif k == j:
            return False
        k = 0

for i in m:
    tr(i)
    print(i)
