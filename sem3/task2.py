"""
Задача №17. Решение в группах
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
"""

my_list = [1, 1, 2, 0, -1, 3, 4, 4]

res = []
for el in my_list:
    if el not in res:
        res.append(el)
print(len(res))