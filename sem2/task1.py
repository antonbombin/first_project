"""
Задача 1 НЕГАФИБОНАЧЧИ по желанию
Задайте число. Составьте список чисел Фибоначчи,
в том числе для отрицательных индексов.
Пример:
для k = 9 список будет выглядеть так:
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
[Негафибоначчи]
"""

a = [0, 1]
k = 9
for i in range(k-2):
    a.append(a[-1] + a[-2])
    a.insert(0,-a[-1])
print(a)