# a1 = int(input())
# a2 = int(input())
# a3 = input()
# if a3 == '/' and a2 == 0:
#     print('на ноль нельзя делить')
# elif a3 == '/':
#     print(a1/a2)
# elif a3 == '*':
#     print(a1*a2)
# elif a3 == '+':
#     print(a1+a2)
# elif a3 == '-':
#     print(a1-a2)
# else:
#     print('Nevernaya operatsiya')
#
# num = int(input("Введите число: "))
# if num == 0:
#     print("вы ввели 0")
# elif num % 2 == 0:
#     print("вы ввели четное число")
# else:
#     print("вы ввели нечетное число")

# for i in range(10):
#     num = int(input("Введите число: "))
#     if num == 0:
#         print("вы ввели 0")
#     elif num % 2 == 0:
#         print("вы ввели четное число")
#     else:
#         print("вы ввели нечетное число")

# while True:
#     num = int(input("Введите число, для выхода введите ноль: "))
#     if num == 0:
#         print("вы ввели 0")
#         break
#     elif num % 2 == 0:
#         print("вы ввели четное число")
#     else:
#         print("вы ввели нечетное число")
#

"""
Задача №1. Решение в группах По данному целому неотрицательному
n вычислите значение n!. N! = 1 * 2 * 3 * … * N
(произведение всех чисел от 1 до N) 0! = 1
Решить задачу используя цикл while Input: 5 Output: 120
"""
# n = int(input("Введите число N: "))
# faktorial = 1
# while n > 1:
#     faktorial *= n
#     n -= 1
# print(faktorial)

"""
Дано натуральное число A > 1. Определите,
каким по счету числом Фибоначчи оно является, 
то есть выведите такое число n, что φ(n)=A. 
Если А не является числом Фибоначчи, выведите число -1. 
Input: 5 Output: 6
"""

# a = int(input("Введите число A: "))
# first = 1
# second = 0
# current = first + second
# n = 3
# while current < a:
#     n += 1
#     second = first
#     first = current
#     current = first + second
# if a != current:
#     print("-1")
# else:
#     print(n)




