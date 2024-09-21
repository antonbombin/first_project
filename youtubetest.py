"""
Допзадание 1 - Пользователь вводит любое число (дробное или целое),
 надо посчитать количество цифр в числе.
Решаем строго математически, обращаться к числу как к строке нельзя.
"""
# while True:
#     try:
#         num = float(input("Введите число: "))
#     except ValueError as e:
#         print(e)
#         print("Must enter int or float")
#         continue
#     count = 0
#     if num == 0:
#         print("1")
#     else:
#         while num > 0:
#             num = num // 10
#             count += 1
#         print(count)
#     answer = input("Continue? Yes or no: ")
#     if answer == 'no':
#         break

"""
Допзадание 2

Валентина прогуляла лекцию по математике.
Преподаватель решил подшутить над нерадивой студенткой и
попросил ее на практическом занятии перечислить все положительные делители некоторых целых чисел.
Для несложных примеров студентка быстро нашла решения (для числа 6 это: 1, 2, 3, 6; а для числа 16 это: 1, 2, 4, 8, 16), но этим все не закончилось.
На домашнее задание ей дали варианты посложнее: 23436, 190187200, 380457890232.
•
Решить такое вручную, как вы понимаете, практически нереально.
Вот Валентина и обратилась к вам за помощью.
Помогите ей.
Постарайтесь найти самое оптимальное решение.
"""

# a = int(input("Введите число делители которого хотите найти: "))
# for i in range(1, a):
#     if a % i == 0:
#         print(i, end=" ")

"""
Задача №1. Решение в группах Дан список чисел. 
Определите, сколько в нем встречается различных чисел.
 Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6
"""

# my_str = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(my_str)))

"""
Задача №2. Решение в группах Дана последовательность из N целых чисел
и число K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, 
K – положительное число. 
Input: [1, 2, 3, 4, 5] k = 2 Output: [4, 5, 1, 2, 3]
"""

# my_list = [1, 2, 3, 4, 5]
# k = 2
# new_list = my_list[k:] + my_list[:k]
# print(new_list)

# my_list = [1, 2, 3, 4, 5]
# k = 2
# b = my_list.copy()
# for i in range(len(my_list)):
#     b[(i + k) % len(my_list)] = my_list[i]
# print(b)

# my_list = [1, 2, 3, 4, 5]
# k = 2
# for i in range(k):
#     a1 = my_list.pop()
#     a2 = my_list.insert(0, a1)
# print(my_list)



