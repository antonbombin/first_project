"""
task 1 lesson 24
"""
# x = int(input("Введите любое число: "))
# num_list = [1431, 46, 2, 15, 4, 13]
# if x in num_list:
#     print(7145)
# else:
#     print(5741)

"""
task 2 lesson 24
"""
# import math
# num_list = [1431, 46, 2, 15, 4, 13]
# print(sum(num_list))
# print(math.prod(num_list))

"""
task 3 lesson 24 - разобрать на уроке
"""
# list_1 = ' < > '
# list_2 = ' ^   '
# list_3 = ' |   '
#
# res_list = 5 * list_1
# res_list2 = 5 * list_2
# res_list3 = 5 * list_3
#
# print(f'{res_list}\n {res_list2}\n {res_list3}\n' * 3)


"""
task 10 lesson 25
"""

# n = 3
# count = 0
# while n > 0:
#     count += 1 / n
#     n -= 1
# print(count)

"""
task 11 lesson 25
"""
# n = 3
# count = 0
# while n >= 0:
#     count += 2 ** n
#     n -= 1
# print(count)

"""
task 12 lesson 25
"""
# n = 3
# count = 0
# while n >= 0:
#     count += 1 + 0.1 * n
#     n -= 1
# print(count)

"""
task 13 lesson 25
"""
# n = 3
# count = 0
# while n > 0:
#     if n % 2 == 0:
#         count -= 1 + 0.1 * n
#         n -= 1
#     else:
#         count += 1 + 0.1 * n
#         n -= 1
# print(count)

"""
task 13 lesson 25 - разобрать
"""
# n = 3
# count = 0
# for i in range(1, n * 2):
#    if i % 2 != 0:
#        count += i
# print(count)

"""
task 1 lesson 26
"""
# str_1 = 'Привет КАк дЕЛа'
# new_str = ''
# for i in str_1:
#     if i.islower() or i == ' ':
#         new_str += i
# print(new_str)

"""
task 2 lesson 26 - разобрать!
"""
# my_str = 'python'
# for i in enumerate(my_str):
#     res = i[:1] + i[:]
#     print(res)


"""
1. Создайте список, содержащий квадраты всех чисел от 1 до 20, но только тех, которые делятся на 3.
"""
# a = [i ** 2 for i in range(21) if i % 3 == 0]
# print(a)

"""
2. Дан список слов. Напишите код, который создает список первых букв каждого слова, если слово начинается с гласной буквы (a, e, i, o, u).
Пример ввода ['apple', 'banana', 'orange', 'umbrella', 'grape', 'elephant'], пример вывода ['a', 'o', 'u', 'e']
"""
# my_list = ['apple', 'banana', 'orange', 'umbrella', 'grape', 'elephant']
# my_list2 = ['a', 'e', 'i', 'o', 'u']
# a = [i[0] for i in my_list if i[0] in my_list2]
# print(a)

"""
task 1 lesson 27
"""
# str_1 = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧЩШЪЫЬЭЮЯ'
# for k in range(11):
#     print(str_1[k] + str_1[k + 11] + str_1[k + 22])

"""
lesson 28
"""

"""
Задание:
• Пользователь вводит от какого числа считать
• Пользователь вводит до какого числа считать
• Программа выводит РАЗ в секунду число (Сколько уже прошло секунд)
"""

# import time
#
# num1 = int(input("Введите от какого числа считать: "))
# num2 = int(input("Введите до какого числа считать: "))
# sec = 0
# for i in range(num1, num2 + 1):
#     time.sleep(1)
#     sec += 1
#     print(sec)






