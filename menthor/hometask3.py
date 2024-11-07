"""
Task 5
"""

# num1 = 4444
# my_str = str(num1)
# print('Успешно') if len(my_str) == 4 else print('Неудача')

# count = 0
# while num1 > 0:
#     num1 = num1 // 10
#     count += 1
# print('Успешно') if count == 4 else print('Неудача')

"""
Task 6
"""
# time = int(input("Введите время в часах: "))
# if not isinstance(time, int) or time <= 0 or time > 23:
#     print("Ошибка")
# elif time >= 7 and time <= 10:
#     print("Пора вставать!")
# else:
#     print("Ты проспал!")

"""
Task 7
"""
# time = int(input("Введите время в часах: "))
# if not isinstance(time, int) or not 0 <= time <= 23:
#     print("Ошибка")
# elif time in range(0, 7):
#     print("Ночь")
# elif time in range(7, 12):
#     print("Утро")
# elif time in range(12, 18):
#     print("День")
# else:
#     print("Вечер")

"""
Task 8
"""
# time_years = input("Введите название времени года: ")
# season = {
#     'Лето': 'Тополиный пух, жара, июль',
#     'Зима': 'Снеговик, снежки и горка',
#     'Осень': 'Пора в школу!',
#     'Весна': 'Весенняя капель',
# }
#
# for k, v in season.items():
#     if k.lower() == time_years.lower():
#         print(v)
#         break
#     else:
#         print("Ошибка")
#         break

"""
task 9 lesson 10
"""


# def check_num(month):
#     if not 1 <= month <= 12:
#         print("Ошибка")
#     elif month in range(6, 9):
#         print("Вы родились летом")
#     elif month in range(9, 12):
#         print("Я тоже люблю осенник листопад")
#     elif month in range(3, 6):
#         print("Подснежник")
#     else:
#         print("К холодам вам не привыкать")
#
#
# month_num = int(input("Введите номер месяца своего рождения: "))
# check_num(month_num)

"""
task 10 lesson 10
"""

# num_years = int(input("Введите год рождения: "))
# if num_years % 4 == 0 or num_years % 100 == 0 and num_years % 400 == 0:
#     print("Вы случайно родились не 29 февраля?")
# else:
#     print("Ничего необычного")


"""
task 11 lesson 10
"""

# num = int(input("Введите число: "))
# if num > 0 and num % 2 == 0:
#     print("Положительное четное число")
# elif num > 0 and num % 2 != 0:
#     print("Положительное нечетное число")
# elif num < 0 and num % 2 == 0:
#     print("Отрицательное четное число")
# elif num < 0 and num % 2 != 0:
#     print("Отрицательное нечетное число")
# else:
#     print("Нулевое число")

"""
Task 12 lesson 10
"""

# num = int(input("Введите целое число: "))
# if not 1 <= num <= 999:
#     print("Ошибка")
# elif num // 10 == 0:
#     print("Цифра")
# elif num // 10 // 10 == 0:
#     print("Двухзначное")
# else:
#     print("Трехзначное")

"""
task 1 lesson 12
"""
# count = 0
# while True:
#     num = int(input("Введите целое число: "))
#     if num < 0:
#         print(count)
#         break
#     else:
#         count = count + num

"""
lesson 13
"""

# number = 7468737
# max_num = 0
#
# for i in str(number):
#     if int(i) > max_num:
#         max_num = int(i)
# print(max_num)
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#
# find_num = 4
# if find_num in numbers:
#     print("Число найдено!")
#
# for i in numbers:
#     if i == find_num:
#         print("Число найдено!")
#         break

"""
task 1 lesson 14
"""
# my_list = [0, 0, 0, 0, 0]
#
# for i in enumerate(my_list, 1):
#     print(f"{i[0]}. {i[1]}")

"""
task 2 lesson 14
"""

# num_list = []
# for i in range(0, 101):
#     num_list.append(i)
# print(sum(num_list))
#
# count = 0
# for i in num_list:
#     count += i
# print(count)

"""
task 3 lesson 14
"""
# num_list = []
# for i in range(1, 498):
#     if i % 2 == 0:
#         num_list.append(i)
# print(num_list)

"""
task 4 lesson 14
"""
# import math
#
# num_list = []
# for i in range(0, 951):
#     if i % 2 != 0:
#         num_list.append(i)
# print(math.prod(num_list))
#
# n = 1
# for el in num_list:
#     n *= el
# print(n)

"""
task 1 lesson 15
"""
# n = 5
# a = 0
# while a <= 5:
#     print(a)
#     a += 1

"""
task 2 lesson 15
"""
# k, n = 2, 5
#
# while k <= n:
#     print(k)
#     k += 1

"""
task 3 lesson 15
"""

# n = 10
# a = 0
# while n >= a:
#     print(n)
#     n -= 1

"""
lesson 16 task 4
"""
# num = 9
# while num >= 3:
#     num /= 3
# if num == 1:
#     print("yes")
# else:
#     print("no")

"""
lesson 16 task 5
"""
# num = 10
# factorial = 1
# while num >= 1:
#     factorial *= num
#     num -= 1
# print(factorial)
# factorial_str = str(factorial)
# # factorial_list = list(factorial_str)
# # print(max(factorial_list))
#
# factorial_list = []
# for i in factorial_str:
#     factorial_list.append(int(i))
# print(max(factorial_list))

"""
lesson 16 task 6
"""
# num = 10
# count = 0
# while num > 0:
#     if num % 2 == 0:
#         count += num
#         num -= 1
#     else:
#         num -= 1
# print(count)

"""
lesson 16 task 7
"""

# k = 1
# n = 9
# count = 0
# while k <= n:
#     if k % 2 != 0:
#         count += k
#         k += 1
#     else:
#         k += 1
# print(count)

"""
lesson 17 task 10
"""
# n = 104
# count = 0
# while n >= 1:
#     count += 1 / n
#     n -= 1
# print(count)

"""
lesson 17 task 11
"""
# n = 4
# count = 0
# while n >= 0:
#     count += 2 ** n
#     n -= 1
# print(count)

# my_list = []
# for i in range(0, n + 1):
#     my_list.append(2 ** i)
# print(sum(my_list))

"""
lesson 17 task 12
"""

# n = 2
# count = 1
# while n >= 1:
#     count += 1 + 0.1 * n
#     n -= 1
# print(count)

"""
lesson 17 task 13
"""

# n = 2
# count = 0
# while n >= 1:
#     if n % 2 == 0:
#         count -= 1 + 0.1 * n
#     else:
#         count += 1 + 0.1 * n
#     n -= 1
# print(count)

"""
Шифрование и дешифрование текста. Напишите программу, которая использует словарь для присвоения "кодов" каждой букве алфавита. 
Например: codes = { 'А': '%', 'а': '9', 'Б': '@', 'б': '#', ... }. Здесь букве 'А' присвоен символ '%', букве 'а' — символ '9', букве 'Б' — символ '@' и т. д.
Программа должна читать строку, и использовать словарь для записи зашифрованной версии строки в другую переменную. 
Каждый символ во второй строке должен быть заменен соответствующим кодом из словаря.
"""

# codes = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '!', 'k': '+',
#          'l': '-', 'm': '/', 'n': '*', 'o': '|', 'p': '\\', 'q': '.', 'r': ',', 's': '}', 't': '{', 'u': '[',
#          'v': ']', 'w': '@', 'x': '#', 'y': '$', 'z': '%', ' ': '&'}
# my_str = 'hello world'
# my_list = list(my_str)
# codes_list = []
# for i in my_list:
#     for k, v in codes.items():
#         if i == k:
#             codes_list.append(v)
# res = ''
# for el in codes_list:
#     res += el
# print(res)
# my_word = list(input("Введите шифр из цифр: "))
# decods_list = []
# for i in my_word:
#     for k, v in codes.items():
#         if i == v:
#             decods_list.append(k)
# decods_res = ''
# for el in decods_list:
#     decods_res += el
# print(decods_res)


"""
1) Напишите код на языке Python, который принимает в качестве 
входных данных последовательность слов, разделенных дефисами,
и печатает слова в последовательности, разделенной дефисами,
после сортировки по алфавиту. Образцы элементов : 
зеленый-красный-желтый-черный-белый 
Ожидаемый результат : белый-желтый-зеленый-красный-черный

2) Напишите код Python, чтобы создать и распечатать список,
значения которого представляют собой квадрат чисел от 1 до 30
(оба включены)  (это задание разбирается в видео).

3) Напишите программу на Python, считающую кол-во гласных,
согласных, цифр, спец. символов в тексте;

4) Напишите программу на Python, считающую кол-во больших и
маленьких букв  (задание разбирается в видео).
"""


"""
Task 1
"""
# my_str = 'зеленый-красный-желтый-черный-белый'
# my_list = my_str.split('-')
# print(sorted(my_list))
# new_str = ''
# for el in my_list:
#     if my_list.index(el) == len(my_list) - 1:
#         new_str += el
#     else:
#         new_str += el + '-'
# print(new_str)

"""
Task 2
"""
# n = 1
# my_list = []
# while n <= 30:
#     my_list.append(n ** 2)
#     n += 1
# print(my_list)

"""
Task 3
"""
# text = input("Введите любую фразу: ")
# count = {}
#
# for i in text:
#     if i not in count:
#         count[i] = 0
#     count[i] += 1
#
#
# for k, v in count.items():
#     print(f'Буква {k} встречается в тексте {v} раз!')

"""
Task 4
"""

# my_str = 'Hello world'
# my_list = list(my_str)
# count_upper = 0
# count_lower = 0
# for el in my_list:
#     if el.isupper():
#         count_upper += 1
#     elif el.islower():
#         count_lower += 1
# print(f'Заглавных букв {count_upper}, строчных букв {count_lower}')


"""
Задание:

Бизнесмен взял ссуду m тысяч рублей в банке под 20% годовых. Через сколько лет его долг превысит s тысяч рублей, если за это время он не будет отдавать долг?

Каждый год урожайность повышается на 5%. Через сколько лет урожай удвоится?

Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована (задание разбирается в видео).

Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран (задание разбирается в видео).
"""

"""
Task 1 les 21
"""
# m = int(input("Введите суммы суды: "))
# s = int(input("Введите сумму долга которую нельзя превысить: "))
# count = 0
# while m < s:
#     m *= 1.2
#     count += 1
# print(count)

"""
task 2 les 21
"""
# m = int(input("Введите урожайность в год: "))
# n = m * 2
# count = 0
# while m <= n:
#     m *= 1.05
#     count += 1
# print(count)

"""
task 4 les 21
"""
# sum_num = sum(range(1, 101))
# print(sum_num)


"""
Вывести на экран все чётные значения в диапазоне от 1 до 497 (это задание разбирается в видео).

Перемножить все нечётные значения в диапазоне от 0 до 9435..

Напишите программу для получения факториала числа.
"""

"""
task 1 les 22
"""
# my_list = []
# for el in range(1, 498):
#     if el % 2 == 0:
#         my_list.append(el)
# print(my_list)

"""
task 2 les 22
"""
# count = 1
# for el in range(1, 96):
#     if el % 2 != 0:
#         count *= el
# print(count)

"""
task 3 les 22
"""
# num = int(input("Введите число факториал которого вы хотите найти: "))
# factorial_num = 1
# while num >= 1:
#     factorial_num *= num
#     num -= 1
# print(factorial_num)

















