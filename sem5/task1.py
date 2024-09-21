# def summ_cycle(num):
#     sum = 0
#     while True:
#         if num == 0:
#             break
#         sum += num
#         num -= 1
#     return sum
#
#
# def summ_rec(num):
#     if num == 0:
#         return 0
#     return num + summ_rec(num - 1)
#
#
#
#
# num = int(input("Введите число: "))
# print(f"Сумма всех чисел от 1 до {num} составляет {summ_cycle(num)}")
# print(f"Сумма всех чисел от 1 до {num} составляет {summ_rec(num)}")


"""
Задача №3. Решение в группах Напишите функцию, которая принимает
одно число и проверяет, является ли оно простым
 Напоминание: Простое число - это число,
которое имеет 2 делителя: 1 и n(само число) Input: 5 Output: yes
"""


# def is_delim(n: int, d= None):
#     if d is None:
#         d = int(n ** 0.5 + 1)
#     if d == 1:
#         return True
#     if n % d == 0:
#         return False
#     return is_delim(n, d - 1)
#
#
# num = int(input("Введите число для проверки: "))
# print(is_delim(num))



# def rec_sum(employees: list) -> int:
#     sum = 0
#     for elem in employees:
#         if isinstance(elem, list):
#             sum += rec_sum(elem)
#         else:
#             sum += elem
#
#     return sum
#
#
#
# a = [[[1, 2], [3, 4, [5, 6, 7]]],[[8, 9, [10, 11]], [12, [13, [[14, 15]]]]]]
#
# print(rec_sum(a))



"""
на входе от пользователя будет строка в виде арифметического
выражения любой длины, записанного по законам математики.
Например, 3 + 3 * 4 - 6 / 2
надо посчитать результат через рекурсию
ответ будет 12
"""

my_str = input("Введите выражение: ")

