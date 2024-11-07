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
lesson 51 task 3 - обсудить
"""

# def factorial_num(n):
#     if n == 0:
#         return 1
#     return n * factorial_num(n - 1)
#
#
# print(factorial_num(15))


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
# print(f(1000))


"""
lesson 51 task 6 -  разобрать
"""

# def f(a, b):
#     if a == 0:
#         return b
#     if a > 0:
#         return f(a // 10, 10 * b + (a % 10))
#
#
# print(f(1392781243, 0))

