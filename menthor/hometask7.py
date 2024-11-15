"""
lesson 39
"""
# import random
# list_num = random.sample(range(-100,101), 5)
# print('Список случайный чисел:', list_num)
# count = 0
# for i in list_num:
#     if i >= 0:
#         count += i
# print('Сумма всех положительных чисел равна:', count)
# max_num = max(list_num)
# min_num = min(list_num)
# print(f'Максимальное число списка: {max_num}, Минимальное число списка: {min_num}')
# max_index = list_num.index(max_num)
# min_index = list_num.index(min_num)
# if min_index > max_index:
#     min_index, max_index = max_index, min_index
# print('Сумма чисел между минимальным и максимальным равна:', sum(list_num[min_index + 1:max_index]))

"""
lesson 40
"""
# with open("res.txt", 'w', encoding="utf-8") as file:
#     try:
#         r = int(input("Введите радиус окружности (см): "))
#         if r < 0:
#             print("Введено некорректное значение!")
#         else:
#             file.write(f'Периметр окружности равен: {(2 * 3.14 * r):.1f} см \n')
#             file.write(f'Площадь окружности равна: {(3.14 * r ** 2):.1f} см \n')
#     except ValueError:
#         print("Допустимы только числовые значения!")

"""
lesson 41
"""


# def read_file(file):
#     try:
#         if '.' in file:
#             expansion = file.split('.')[-1]
#             print(f'Расширение файла: {expansion}')
#         else:
#             print("Невозможно определить расширение файла")
#
#         with open(file, 'r', encoding="utf-8") as text:
#             data_file = text.read()
#             print(data_file)
#     except FileNotFoundError:
#         print(f'Файл {file} не найден')
#
#
# read_file(input("Введите название файла: "))


"""
lesson 42
"""


# def sum_sim_num(file):
#     with open(file, 'r', encoding="utf-8") as text:
#         list_num = [i for i in text.read()]
#         simular_elem = {}
#
#         for i in list_num:
#             if i not in simular_elem:
#                 simular_elem[i] = 0
#             simular_elem[i] += 1
#
#         for k, v in simular_elem.items():
#             if v > 1:
#                 print(f'Число {k} встречается {v} раза!')
#
#
# sum_sim_num('list_num.txt')

"""
lesson 43 - разобрать!
"""


def shortener(st: str) -> None:
    """
    Из строки убираем часть текста в скобках.

    В функцию передается строка, внутри функции создаем новую строку и добавляем в неё текст, который записан за
    пределами скобок.

    Args:
         st: str (Строка содержащая текст в котором часть текста записана в скобках)
    """
    new_str = ''
    for elem in st:
        if elem == '(':
            new_str = st[:st.index(elem)] + st[st.index(')') + 1:]
    print(new_str)


shortener('Дмитрий считает что когда текст пишут в скобках (как вот тут, например) его читать не нужно')


"""
lesson 44 - разобрать
"""


# def camel(st):
#     new_st = ''
#     for elem in st:
#         if st.index(elem) % 2 != 0:
#             new_st += elem.upper()
#         elif elem == ' ' or elem == ',':
#             new_st += elem
#         else:
#             new_st += elem
#     print(new_st)
#
#
# camel('чередующиебуквызаписываем')


"""
lesson 45 task 1
"""


# def sum_range(start, end):
#     if end < start:
#         start, end = end, start
#     sum_num = 0
#     for i in range(start, end + 1):
#         sum_num += i
#
#     return sum_num
#
#
# print(sum_range(1, 50))

"""
lesson 45 task 2
"""

# def max_num(a,b,c):
#     return max(a, b, c)
#
#
# print(max_num(5, 10000, 100))


"""
lesson 45 task 3
"""
# from datetime import datetime
#
# def difference_time():
#     time1 = datetime.now()
#     time2 = datetime(2023, 10, 31)
#     print(time1 - time2)
#
#
# difference_time()

"""
lesson 46 
"""


# def is_prime(n):
#     count = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             count += 1
#     if count == 2:
#         return True
#     else:
#         return False
#
#
# print(is_prime(211))


"""
lesson 47 task 1
"""

# def check_register(st):
#     big_letter = 0
#     small_letter = 0
#     for elem in st:
#         if elem.isalpha():
#             if elem.islower():
#                 small_letter += 1
#             else:
#                 big_letter += 1
#     print(f'Количество символов в верхнем регистре: {big_letter}\nКоличество строчных букв: {small_letter}')
#
#
# check_register('Быстрая Лиса Бровей')

"""
lesson 47 task 2
"""

# def check_unique(num_list):
#     return list(set(num_list))
#
#
# num = [1, 2, 3, 3, 3, 3, 4, 5, 5, 6]
# print(check_unique(num))

"""
lesson 48 task 1
"""


# def check_num(start, end, num):
#     if num in range(start, end + 1):
#         print("Число находится в заданном диапазоне!")
#     else:
#         print("Число не находится в заданном диапазоне!")
#
#
# start_range = int(input("Введите начальную цифру диапазона: "))
# end_range = int(input("Введите последнюю цифру диапазона: "))
# number = int(input("Введите число для проверки: "))
# check_num(start_range, end_range, number)


"""
lesson 48 task 2
"""
# def is_prime(n):
#     count = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             count += 1
#     if count == 2:
#         return True
#     else:
#         return False
#
#
# print(is_prime(211))

"""
lesson 48 task 3
"""

# def check_even(st):
#     new_st = []
#     for i in st:
#         if i % 2 == 0:
#             new_st.append(i)
#
#     return new_st
#
#
# num_st = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(check_even(num_st))

"""
lesson 49 task 1
"""

# def sort_st(st):
#     new_list = []
#     for i in st.split('-'):
#         new_list.append(i)
#     new_st = '-'.join(sorted(new_list))
#     print(new_st)
#
#
# sort_st('зелёный-красный-жёлтый-чёрный-белый')


"""
lesson 49 task 2
"""

# def diff_time(time1, time2):
#     diff = time2 - time1
#
#     days = diff // 86400
#     diff %= 86400
#     hours = diff // 3600
#     diff %= 3600
#     minutes = diff // 60
#     seconds = diff % 60
#
#     format_time = f'{days} дней, {hours} часов, {minutes} минут, {seconds} секунд'
#     return format_time
#
#
# time_1 = int(input("Введите первое время в секундах: "))
# time_2 = int(input("Введите второе время в секундах: "))
# print(diff_time(time_1, time_2))

"""
lesson 49 task 3
"""
# import random
#
#
# def check_num():
#     while True:
#         rnd_num = random.randint(0, 1000)
#         while True:
#             num = int(input("Угадай загаданное число: "))
#             if num == rnd_num:
#                 print("Поздравляю ты угадал число!")
#                 break
#             elif num < rnd_num:
#                 print("Загаданное число больше твоего, попробуй ещё!")
#             else:
#                 print("Загаданное число меньше твоего, попробуй ещё!")
#
#         res = input("Желаете продолжить? yes - продолжить, exit - завершить: ")
#         if res == 'yes':
#             continue
#         elif res == 'exit':
#             break
#         else:
#             print('Вы ввели неверную команду!')
#
#
# check_num()


"""
lesson 50
"""

# def ladder_num(n, floor):
#     count = 0
#     if n == 0:
#         return 1
#     for i in range(floor, n + 1):
#         count += ladder_num(n - i, i + 1)
#     return count
#
#
# print(ladder_num(6, 1))


