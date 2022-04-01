"""
Используя функцию sorted() и lambda-функцию, отсортируйте список кортежей по последнему символу их второго элемента.
"""

l = (["alpha", "betta", "gamma"], ["first", "second", "third"], ["Darina", "Irina", "Maksym"])

print(l)

res = sorted(l, key=lambda i: i[1][-1])
print(res)