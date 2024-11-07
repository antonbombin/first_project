"""
Дано число.
Если оно больше 100 или меньше -100,
вывести на экран символ "-",
иначе вывести на экран символ "+" (это задание разбирается в видео);
"""

# num = int(input("Введите число: "))
# if num > 100 or num < -100:
#     print("-")
# else:
#     print("+")

"""
Дано положительное число N. Вывести все числа от 0 до N с помощью цикла while
"""

# num = int(input("Введите число: "))
#
# count = 0
# while count <= num:
#     print(count)
#     count += 1

"""
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована
"""
# my_list = ('0000', '0000', '0000', '0000', '0000')
# for i in enumerate(my_list):
#     print(i[0]+1, i[1])

# for i in range(1, 6):
#     print(i, '0000')

"""
Посчитать количество одинаковых элементов в списке. 
Список берётся из файла. Пример: в файле записанно число 172727, 
программа должна преобразовать это число в список и найти кол-во одинаковых аргументов.
"""

# def sum_list(numbers):
#     str_num = str(numbers)
#     list_num = []
#     for i in str_num:
#         list_num.append(int(i))
#     set_num = set(list_num)
#     res = len(list_num) - len(set_num)
#     return res
#
#
# num = 172727
# print(sum_list(num))



"""
Напишите функцию sum_range(start, end), 
которая суммирует все целые числа от значения «start» до величины «end» включительно.
Если пользователь задаст первое число большее чем второе, просто поменяйте их местами
"""

# def sum_range(start,end):
#     sum_num = 0
#     if start > end:
#         for elem in range(end, start + 1):
#             sum_num += elem
#     else:
#         for elem in range(start, end + 1):
#             sum_num += elem
#     return sum_num
#
#
# num_1 = int(input("Введите число 1: "))
# num_2 = int(input("Введите число 2: "))
# res = sum_range(num_1, num_2)
# print(res)

"""
Евгению предоставили строку, состоящую из русских букв разных регистров, 
и попросили очистить ее от заглавных литер. Помогите Евгению решите задачу. 
Пример: >>Привет КАк дЕЛа? <<ривет к да?
"""

# my_str = 'Привет КАк дЕЛа'
# format_str = list(my_str)
# new_str = []
# for elem in format_str:
#     if elem.islower() or elem == ' ':
#         new_str.append(elem)
#
#
# res = ""
# for elem in new_str:
#     res += elem
#
# print(res)

"""
Найдите сумму и произведение элементов списка. Результаты вывести на экран.
"""

# my_str = [1, 2, 5, 5, 7, 8]
#
# sum_str = 0
# multiplay_str = 1
# for elem in my_str:
#     sum_str += elem
#     multiplay_str *= elem
#
# print(sum_str)
# print(multiplay_str)

"""
Задание: 

Запрашиваем число x

Считаем уравнение x^2 + 48x - 19 (вместо x число пользователя)

Выводим результат
(это задание разбирается в видео).
"""

# num = int(input("Entered num: "))
# print(num**2 + 48 * num - 19)






