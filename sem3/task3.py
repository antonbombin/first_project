"""
Задача №19. Решение в группах
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
"""

my_list = [1, 2, 3, 4, 5]
k = 3
new_list = my_list[k:] + my_list[:k]
print(new_list)

for _ in range(k - 1):
    last = my_list.pop()
    my_list.insert(0, last)
print(my_list)
