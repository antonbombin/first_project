"""
Задача №23. Решение в группах
Дан массив, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
"""
my_list = [0, -1, 5, 2, 3]
counter = 0
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i - 1]:
        counter += 1
print(counter)
