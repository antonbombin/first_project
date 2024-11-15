"""
lesson 51 task 1
1) Посчитать сумму четных чисел для промежутка от 1 до n (n задаётся пользователем)
"""


# def sum_num(n):
#     if n == 0:
#         return 0
#     elif n % 2 != 0:
#         return sum_num(n - 1)
#     elif n % 2 == 0:
#         return sum_num(n - 2) + n
#
#
#
# print(sum_num(5))


"""
lesson 51 task 2
"""

"""Fn = Fn-1 + Fn-2"""

# def fibo(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibo(n - 1) + fibo(n - 2)
#
#
# print(fibo(17))


"""
lesson 51 task 3 
"""

# def factorial_num(n):
#     if n < 10:
#         return 1
#     elif n % 2 != 0 and n % 15 == 0:
#         return n * factorial_num(n - 1)
#     return factorial_num(n - 1)
#
#
# print(factorial_num(45))


"""
lesson 51 task 4
"""

# def f(n):
#     if n <= 1:
#         return 1
#     elif n % 2 == 0:
#         return 3 * n + f(n - 2)
#     else:
#         return 4 * f(n // 2)
#
#
# print(f(42))


"""
lesson 51 task 5
"""

# def f(n):
#     if n == 0:
#         return 0
#     elif n % 2 != 0:
#         return f(n - 1) + 1
#     else:
#         return f(n // 2)
#
#
# count = 0
# for i in range(1, 1_001):
#     if f(i) == 2:
#         count += 1
# print(count)

"""
lesson 51 task 6 
"""

# def f(a, b):
#     if a == 0:
#         return b
#     if a > 0:
#         return f(a // 10, 10 * b + (a % 10))
#
#
# numbers = []
# count = 0
# while True:
#     if f(count, 0) == 1392781243:
#         numbers.append(count)
#         count += 1
#     count += 1
#
# print(min(numbers))


# def sum_odd(ls):
#     if len(ls) == 0:
#         return 0
#     elif ls[0] % 2 == 0:
#         return sum_odd(ls[1:])
#     elif ls[0] % 2 != 0:
#         return ls[0] + sum_odd(ls[1:])
#
#
# print(sum_odd([1, 2, 3, 4]))

"""
lesson 52 
"""

# def piramid(row, pos):
#     if row == 0 and pos == 0:
#         return 0
#     elif pos == 0:
#         return piramid(row - 1, pos) * 0.5 + 0.5
#     elif row == pos:
#         return piramid(row - 1, pos - 1) * 0.5 + 0.5
#     else:
#         return piramid(row - 1, pos) * 0.5 + 0.5 + piramid(row - 1, pos - 1) * 0.5 + 0.5
#
#
# print(piramid(30, 5))


# def W(row, pos):
#     count_row = 0
#     count_pos = 0
#     result = 0
#     if pos == 0:
#         while row > 0:
#             count_row = (count_row + 1) / 2
#             row -= 1
#         return count_pos + count_row
#     elif row == pos:
#         while pos > 0:
#             count_pos = (count_pos + 1) / 2
#             pos -= 1
#         return count_pos + count_row
#     else:
#         while row > 0 or pos > 0:
#             if row == 1:
#                 result += ((count_row + 1) / 2) - count_row * 0.5
#                 row -= 1
#             elif pos == 0:
#                 count_row = (count_row + 1) / 2
#                 result += count_row
#                 row -= 1
#             else:
#                 count_row = (count_row + 1) / 2
#                 count_pos = (count_pos + 1) / 2
#                 result += (count_row + count_pos)
#                 pos -= 1
#                 row -= 1
#         return result
#
# print(W(3, 1))


"""
1) Написать свой декоратор для функции (У каждого разный). Не писать декоратор подсчёта времени выполнения функции и проверки на чётность/нечётность.
"""

# def bug_fixes(func):
#     def wrapper(*args, **kwargs):
#         try:
#             result = func(*args, **kwargs)
#             return result
#         except Exception as e:
#             print(func.__name__, e)
#
#     return wrapper
#
# @bug_fixes
# def fibo(n):
#     n / 0
#     if n == 1:
#         return 1
#     return fibo(n - 1) + fibo(n - 2)
#
# @bug_fixes
# def base():
#     a = 70 / 70
#     return a
#
#
# print(fibo(17))
# print(base())





