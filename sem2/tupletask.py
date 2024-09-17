# internal_ids = (151, 245)
# external_ids = (624, 451, 941)
# объединение кортежей
# all_ids = internal_ids + external_ids
#
# print(all_ids)

# posts_ids = (151, 245)
# изменение кортежа через перевод в список
# posts_ids_list = list(posts_ids)
# posts_ids_list.append(351)
#
# print(posts_ids_list)
#
# posts_ids_tuple = tuple(posts_ids_list)
#
# print(posts_ids_tuple)

# Кортеж словарей, где можно изменять значения
# users = (
#     {
#         'user_id': 134,
#         'user_name': 'Alice'
#     },
#     {
#         'user_id': 831,
#         'user_name': 'Bob'
#     }
# )
#
# print(users[1]['user_id'])
#
# users[1]['user_id'] = 100
#
# print(users[1]['user_id'])

# my_nums = (10, 5, 100, 0, 5, 5)
# действия с кортежом поиск количества элементов в кортеже
# print(my_nums.count(5))
# поиск индекса определенного элемента
# print(my_nums.index(5))
#
# index_one = my_nums.index(5)
# index_two = my_nums.index(5, index_one + 1)
# index_three = my_nums.index(5, index_two + 1)
#
# print(index_two)

# my_nums = (10, 5, 100, 0, 5, 5)
# # Изменение элементов кортежа, через конвертацию в список и обратно
# my_list = list(my_nums)
#
# my_list.append(7)
#
# my_nums = tuple(my_list)
#
# print(my_nums)

"""
Набор Set - неупорядоченная последовательность элементоа (уникальных), изменять наборы можно
"""

# my_set = set()
# Создание пустого набора, обычно набор ставится в {}
# print(my_set)
# print(type(my_set))
#
# photo_sizes = {'1920x1080', '800x600'}
# other_sizes = {'800x600', '1024x768'}
# # Объединение наборов
# all_sizes = photo_sizes.union(other_sizes)
#
# print(all_sizes)
# # Пересечение наборов
# common_s = photo_sizes.intersection(other_sizes)
#
# print(common_s)

# nums = {10, 5, 35}
# other_nums = {20, 5, 12, 10, 35}
# # Проверяем входит ли один наблор в другой набор
# res = nums.issubset(other_nums)
# print(res)

"""
Практика наборов
"""

# my_set = {'abc', 'd', 'f', 'y'}
# other_set = {'a', 'f', 'd'}

# print(my_set.intersection(other_set)) # пересечение множеств
#
# print(my_set.union(other_set)) # оба множества объединение
#
# print(other_set.issubset(my_set)) #Является ли множество подмножеством другого
#
# print(my_set.issuperset(other_set)) #включает ли одно множество другое в себя

# print(my_set.difference(other_set)) #Элементы отличающиеся в наборе
#
# my_set.discard('d') # Удаление элемента из набора
# print(my_set)
#
# copied_set = my_set.copy()
#
# my_set.add('t')
# copied_set.add('l')

# print(my_set)
# print(copied_set)
""" Симметричная разница """
# a = {'abc', 'd', 'f', 'y'}
# b = {'abc', 'd', 'f', 'l'}
#
# print((a | b) - (a & b))
# print(a.symmetric_difference(b))
#

# nums = {5, 10, 0, 12}
# nums.add(8)
#
# nums2 = {14, 7, 9, 5, 0}
#
# nums3 = list(nums & nums2)
#
# print(nums3)

"""
Диапазоны range - упорядоченная неизменяемая последовательность элементов
"""

# my_range = range(10, 20, 3) #нижняя граница, верхняя и шаг
#
# print(type(my_range)) #тип рендж
#
# print(my_range) #тот же диапазон не раскрывается только
#
# print(list(my_range)) #перебор элементов диапазона в список

# for n in range(5):
#     print(n)
#
# for n in range(12, 25, 5):
#     print(n)

# my_range = range(10, 30, 3)
#
# print(my_range.start)
# print(my_range.stop)
# print(my_range.step)
#
# print(my_range.index(13)) #поиск индекса элемента
#
# print(my_range.count(10))

# my_list = list()
#
# for i in range(4, 20, 2):
#     my_list.append(i)
#
# print(my_list)

"""
Встроенная функция zip
"""

# fruits = ['apple', 'banana', 'lime']
# quantities = [100, 70, 50]
#
# fruit_qtys_zip = zip(fruits, quantities)
#
# print(fruit_qtys_zip) # <zip object at 0x000002867B97E900>
#
# fruit_qtys_list = list(fruit_qtys_zip)
#
# print(fruit_qtys_list) # [('apple', 100), ('banana', 70), ('lime', 50)]
# # получаем список кортежей с помощью зип

# fruits = ['apple', 'banana', 'lime', 'orange']
# quantities = [100, 70, 50, 20]
#
# fruit_qtys_zip = zip(fruits, quantities)
#
# print(fruit_qtys_zip)
#
# fruit_qtys_list = dict(fruit_qtys_zip)
#
# print(fruit_qtys_list)

# store_things = ['coat', 't-shirt', 'jacket', 'glasses']
#
# store_price = [100, 30, 80, 50]
#
# store_things_price_zip = zip(store_things, store_price)
#
# # store_things_price_list = list(store_things_price_zip)
# # print(store_things_price_list)
#
# store_things_price_dict = dict(store_things_price_zip)
# print(store_things_price_dict)

"""
id - адрес объектов
"""

# my_num = 10
# print(id(my_num))
# #140735700011736
# other_num = 10
# print(id(other_num))
# #140735700011736
# print(id(10))
# #140735700011736

# info = {
#     'name': 'Bogdan',
#     'is_instructor': True
# }
#
# info_copy = info
# info['reviews_qty'] = 5
# info_copy['reviews_qty'] = 100
#
# print(info['reviews_qty']) #100
# print(info_copy['reviews_qty']) #100

"""
После копирования изменяемых объектов изменения отражаются на всех копиях
Как избежать изменений копий
"""

# info = {
#     'name': 'Bogdan',
#     'is_instructor': True
# }
#
# info_copy = info.copy() # через копи это можно сделать
#
# info_copy['reviews_qty'] = 5
#
# print(info_copy)
# print(info)
"""
Изменение копии через глубокую копию дип
"""
# from copy import deepcopy
#
# info = {
#     'name': 'Bogdan',
#     'is_instructor': True,
#     'reviews': []
# }
#
# info_deepcopy = deepcopy(info)
# info_deepcopy['reviews'].append('Great course!')
#
# print(info)
#
# print(info_deepcopy)

# from copy import deepcopy

# info = {
#     'name': 'Bogdan',
#     'is_instructor': True,
#     'reviews': []
# }
#
# info_copy = info.copy()
# info_copy['reviews'].append('Great course!')
# info['reviews'].append('Super')
#
# info['new key'] = 10
#
# print(info)
#
# print(info_copy)

"""
Функции - блок кода, который можно выполнять МНОГОКРАТНО!
Функция это объект!
"""
# def sum(a, b):
#     c = a + b
#     print(c)
#
# a = 5
# b = 3
# sum(a, b)
#
# a = 8
# b = 12
# sum(a, b)

"""
Передача неизменяемых объектов
"""
# def my_fn(a, b):
#     a = a + 1
#     c = a + b
#     return c
#
# num_one = 10
# num_two = 5
#
# res = my_fn(num_one, num_two)
# print(res) # 15
# print(num_one) #10

"""
Передача изменяемых объектов
"""
# def increase_person_age(person):
#     print(id(person))
#     person['age'] += 1
#     return person
#
# person_one = {
#     'name': 'Bob',
#     'age': 21
# }
#
# print(id(person_one))
#
# increase_person_age(person_one)
# print(person_one['age']) #22

"""
Внутри функции не рекомендуется изменять внешние объекты, лучше создавать копию
и лучше deepcopy
"""
# def merge_lists_to_dict(fruits, colors):
#     new_merge_lists = zip(fruits, colors)
#     return dict(new_merge_lists)
#
#
# lists_one = ('banana', 'cherry', 'watermellow')
# lists_two = ('yellow', 'red', 'green')
#
# merge_lists_to_dict(lists_one, lists_two)
# print(merge_lists_to_dict(lists_one, lists_two))
#
# res_two = merge_lists_to_dict(['abc'], [{}, True, 100])
# print(res_two)
#
# res_three = merge_lists_to_dict([10, True, 100], ['abc'])
# print(res_three)

"""
Аргументы функций
"""
# Объединение аргументов в кортеж
# def sum_nums(*args): # * объекдиняет все аргументы
#     print(args) # (2, 3, 7)
#     print(type(args)) # class tuple
#
#     print(args[0]) # 2
#     return sum(args)
#
# print(sum_nums(2, 3, 7)) # 12

"""
Позиционные аргументы (порядок следования аргументов важен при вызове функций и количество)
"""
# def get_posts_info(name, posts_qty):
#     info = f"{name} wrote {posts_qty} posts"
#     return info
#
# info = get_posts_info('Anton', 28)
# print(info) # Anton wrote 28 posts

"""
Аргументы с ключевыми словами (порядок аргументов не важен, код более читабельный)
"""
# def get_posts_info(name, posts_qty):
#     info = f"{name} wrote {posts_qty} posts"
#     return info
#
# info = get_posts_info(name='Anton', posts_qty=28)
# print(info) # Anton wrote 28 posts

# def get_posts_info(name, posts_qty):
#     info = f"{name} wrote {posts_qty} posts"
#     return info
#
# info = get_posts_info(posts_qty=28, name='Anton')
# print(info) # Anton wrote 28 posts

"""
Объединение аргументов в dict
"""
# def get_posts_info(**person):
#     print(person) # {'name': 'Anton', 'posts_qty': 28}
#     print(type(person)) # <class 'dict'>
#     info = (
#         f"{person['name']} wrote "
#         f"{person['posts_qty']} posts"
#     )
#     return info
#
# info = get_posts_info(name='Anton', posts_qty=28)
# print(info) # {'Anton wrote28 posts'}

# def merge_lists_to_dict(list_one, list_two):
#     return dict(zip(list_one, list_two))
#
# res_one = merge_lists_to_dict(list_one=['a', 'b', 'c'], list_two=[10, True, 100])
# print(res_one)
#
# res_two = merge_lists_to_dict(['a', True, 100], list_two=['abc'])
# print(res_two)

# def update_car_info(**car):
#     car['is_available'] = True
#     return car
#
# print(update_car_info(brand='BMW', price=10000))

"""
Значения параметров по умолчанию (дефолтное значение)
"""
# def mult_by_factor(value, multiplier=3): #наличие значения по умолчанию для параметра функции делает его необязательным
#     return value * multiplier
#
# print(mult_by_factor(10, 2)) # 20
# print(mult_by_factor(5)) #15

# from datetime import date
#
# def get_weekday():
#     return date.today().strftime('%A')
#
# def create_new_post(post, weekday=get_weekday()):
#     post_copy = post.copy()
#     post_copy['created_on_weekday'] = weekday
#     return post_copy
#
# initial_post = {
#     'id': 243,
#     'author': 'Anton'
# }
#
# post_with_weekday = create_new_post(initial_post)
# print(post_with_weekday) # {'id': 243, 'author': 'Anton', 'created_on_weekday': 'Tuesday'}

"""
Колбэк функция
"""
# def other_fn():
#     # some actions...
#     pass
#
# def fn_with_callback(callback_fn):
#     callback_fn()
#
# fn_with_callback(other_fn)
"""
В теле второй функции вызывается колбэк функция
"""
#
# def print_number_info(num):
#     if (num % 2) == 0:
#         print("Entered number is even")
#     else:
#         print("Entered number is odd")
#
#
# def print_square_num(num):
#     print("Square of the num is", num * num)
#
#
# def process_number(num, callback_fn):
#     callback_fn(num)
#
#
# entered_num = int(input('Entered any number: '))
#
# process_number(entered_num, print_number_info)
# process_number(entered_num, print_square_num)


"""
1. Называть функции исходя из выполняемых задач
2. Название функции начинать с глагола
3. Одна функция должна выполнять одну задачу
4. Не рекомендуется изменять внешние относительно функции переменные
"""

"""
Документация функции docstring - используется для документирования функций, классов, модулей
"""

# def print_number_info(num):
#     """
#     Print whether number is even or odd
#
#     Args:
#         num (int): Number to be evaluated
#     """
#     if (num % 2) == 0:
#         print("Num is even")
#     else:
#         print("Num is odd")
#
#
# print_number_info(20)


"""
Глобальные и локальные переменные
"""
#
# c = 5
#
# # def my_fn(a, b):
# #     d = 10
# #     print(c)
# #     print(a, b)
# #     print(dir())
# #
# #
# # my_fn(3, 5)

"""
Операторы 
"""

# Арифметические: + - * /
# Сравнения: == != > <
# Логические: not, and, or
# Текстовые: not, and, or, is, is not, in, not in

# my_num = 10
# print(+ my_num)
#
# my_bool = True
# print(+my_bool)

# my_num = 10
# унарные операторы
# print(not my_num)

"""
Бинарные операторы =, +, +=, ==, and
"""

# set_one = {10, 'abc', 50, True}
# set_two = {50, 'abc', 10, True}
#
# print(set_one == set_two) #True
# print(set_one.__eq__(set_two)) #True
#
# print(set_one is set_two) #False
#
# print('abc' in set_one) #True
# print(10 in set_two) #True
# print(1000 in set_one) #False
# # print([] in set_one) #TypeError: unhashable type: 'list'

"""
Ложные значения - значение, которое при приведении к логическому типу дает False, является ложным
"""

# print(bool(0))
# print(bool(0.0))
# print(bool(0j))
#
# print(bool(None))
#
# print(bool({}))
# print(bool([]))
# print(bool(()))
# print(bool(set()))
# print(bool(range(0)))
# print(bool(''))

# print(not not {'a': 10})

# my_list = [1, 2]
# # Ложные значения в условных функциях if
# if len(my_list) > 0:
#     print("List has elements")

"""
Логические операторы - not, and, or
"""
#
# my_dict = {'a': 5, 'b': True}
#
# my_dict_two = {'b': True, 'a': 5}
#
# my_dict == my_dict_two and print("Dicts are equle")

"""
Оператор распаковки словаря **
"""
#
# button = {
#     'width': 200,
#     'text': 'Buy'
# }
#
# red_button = {
#     **button,
#     'color': 'red'
# }
# """Если бы у словаря button был бы ключ 'color', его значение было бы перезаписано """
# print(red_button)
# # {'width': 200, 'text': 'Buy', 'color': 'red'}
#
# print(button)
# # {'width': 200, 'text': 'Buy'}

"""
Объединение словарей с помощью **
"""
# button_info = {
#     'text': 'Buy'
# }
#
# button_style = {
#     'color': 'yellow',
#     'width': 200,
#     'height': 300
# }
#
# button = {
#     **button_info,
#     **button_style
# }
#
# print(button)
# # {'text': 'Buy', 'color': 'yellow', 'width': 200, 'height': 300}
#
# button_new = button_info | button_style
#
# print(button_new)
# # {'text': 'Buy', 'color': 'yellow', 'width': 200, 'height': 300}

"""
Инструкция del - удаление элементов
"""
#
# my_list = [1, 2]
#
# del my_list[0]
# my_list.__delitem__(0)
#
# print(my_list)

"""
Форматирование строк
"""
# my_name = 'Anton'
# my_hobby = 'running'
# time = 8
#
# info = my_name + ' likes ' + my_hobby + ' ' + 'at ' + str(time) + " o'clock "
#
# print(info)
#
# info_two = f"{my_name} likes {my_hobby} at {time} o\'clock".upper()
# print(info_two)

"""
Лямбда функции
"""
# lambda a, b: a * b

# def mult(a, b):
#     return a * b
#
# mult = lambda a, b: a * b
#
# print(mult(10, 5))


# def greeting(greet):
#     return lambda name: f"{greet}, {name}!"
#
#
# morning_greeting = greeting("Good Morning")
#
# print(morning_greeting('Anton'))
# # Good Morning, Anton!
#
# evening_greeting = greeting("Good Evening")
#
# print(evening_greeting('Anton'))
# # Good Evening, Anton!

"""
Исключение ошибок в коде
"""
# try:
#     print(10 / 2)
# except Exception as e:
#     print(e)
#
# try:
#     print(10 / 2)
# except:
#     print("Some error occurred")

"""
Генерация ошибки через Raise
"""

# def divide_nums(a, b):
#     if b == 0:
#         raise ValueError("Second argument can't be 0")
#     return a / b
#
# try:
#     divide_nums(10, 0)
# except ValueError as e:
#     print(e)
#
# print("Continue...")


# def image_info(img):
#     if ('image_id' not in img) or ('image_title' not in img):
#         raise TypeError("Keys image_id and image_title must be present")
#
#     return f"Image {img['image_title']} has id {img['image_id']}"
#
#
# print(image_info({'image_title': 'my_cat', 'image_id': 123}))
#
# try:
#     print(image_info({'image_id': 123}))
# except TypeError as e:
#     print(e)

"""
Распаковка словаря - извлечение значений и присвоение переменным
"""
# my_fruits = ['apple', 'banana', 'lime']

# my_apple = my_fruits[0]
# my_banana = my_fruits[1]
# my_lime = my_fruits[2]
#
# print(my_apple) #apple
# print(my_banana) #banana
# print(my_lime) # lime

# my_apple, my_banana, my_lime = my_fruits # пример распаковки
# print(my_apple) #apple
# print(my_banana) #banana
# print(my_lime) # lime

# my_apple, *remaining_fruits = my_fruits
# # пример использования *
# print(my_apple)
# print(remaining_fruits)

"""
Распаковка словаря в аргументы с ключевыми словами
"""
# user_profile = {
#     'name': 'Anton',
#     'comments_qty': 23
# }
#
#
# def user_info(name, comments_qty=0):
#     if not comments_qty:
#         return f"{name} has no comments"
#
#     return f"{name} has {comments_qty} comments"
#
#
# print(user_info(**user_profile)) #Anton has 23 comments

"""
Распаковка списка в позиционные аргументы
"""
# user_data = ['Anton', 23]
#
# def user_info(name, comments_qty):
#     if not comments_qty:
#         return f"{name} has no comments"
#
#     return f"{name} has {comments_qty} comments"
#
# print(user_info(*user_data)) # Anton has 23 comments

"""
Условные функции

if Условие: 
# блок кода, выполняемый однократно, если Условие правдиво 
"""
# my_number = 25
#
# if my_number > 0:
#     print(my_number, "is positive number!")

# num_one = 10
# num_two = 5
#
# if (num_one > 0
#         and num_two > 0
#         and isinstance(num_one, int)
#         and isinstance(num_two, int)):
#     print("Both numbers are ints and possitive")

# my_phone = {
#     'price': 200
# }
#
# if my_phone.get('brand'):
#     print("Phone's brand is", my_phone['brand'])
# else:
#     print("There is no phone brand")

# def nums_info(a, b):
#     if (type(a) is not int) or (type(b) is not int):
#         return "Один из аргументов не целое число"
#
#     if a >= b:
#         return f"{a} больше или равно {b}"
#
#     return f"{a} меньше {b}"

# def nums_info(a, b):
#     if (type(a) is not int) or (type(b) is not int):
#         info = "Один из аргументов не целое число"
#     elif a >= b:
#         info = f"{a} больше или равно {b}"
#     else:
#        info = f"{a} меньше {b}"
#     return info
#
#
# print(nums_info(True, 10)) # Один из аргументов не целое число
# print(nums_info(10, 2)) # 10 больше или равно 2
# print(nums_info(4,15)) # 4 меньше 15


# def route_info(route):
#     if ('distance' in route) and (type(route['distance']) == int):
#         return f"Distance to your destination is {route['distance']}"
#
#     if ('speed' in route) and ('time' in route):
#         return f"Distance to your destination is {route['speed'] * route['time']}"
#
#     else:
#         return "No distance info is available"
#
#
# print(route_info({'distance': 15})) #Distance to your destination is 15
#
# print(route_info({'speed': 20, 'time': 3})) #Distance to your destination is 60
#
# print(route_info({'my_speed': 30})) #No distance info is available

"""
Тернарный оператор (условное выражение) - у тернарного оператора три операнда
Конструкция с тернарным оператором - выражение
"""

# my_image = ('1920', '1080')
#
# info = f"{my_image[0]}x{my_image[1]}" \
#     if len(my_image) == 2 else "Incorrect image formatting"

# if len(my_image) == 2:
#     info = f"{my_image[0]}x{my_image[1]}"
# else:
#     info = "Incorrect image formatting"
#
# print(info)
#
# my_str = "Very, very, very, Very, very, very, Very, very, very, very, very, very, very long string"
# print(len(my_str))
# print('String is long' if len(my_str) > 79 else 'String is short')

"""
Циклы 
"""

# for in для списков
# my_list = [True, 10, 'abc', {}]
#
# for elem in my_list:
#     print(elem)

# for in для кортежей

# video_info = ('1920x1080', True, 27)
#
# for elem in video_info:
#     print(elem)

# for in для словарей

# my_object = {
#     'x': 10,
#     'y': True,
#     'z': 'abc'
# }
#
# for key in my_object:
#     print(key, my_object[key])

# my_object = {
#     'x': 10,
#     'y': True
# }
#
# for key, value in my_object.items():
#     print(key, value)


# def dict_to_list(dict_to_convert):
#     list_for_conversion = []
#     for key, value in dict_to_convert.items():
#         if type(value) == int:
#             value *= 2
#         list_for_conversion.append((key, value))
#
#     return list_for_conversion
#
#
# print(dict_to_list({'a': 5, 'b': [], 'c': 100}))

# def filter_list(list_to_filter, value_type):
#     filtered_list = []
#     for elem in list_to_filter:
#         if type(elem) == value_type:
#             filtered_list.append(elem)
#         # No recommended
#         # if isinstance(elem, value_type):
#         #     filtered_list.append(elem)
#
#     return filtered_list
#
#
# print(filter_list([35, True, 'abc', 10], int))
# print(filter_list([35, True, 'abc', 10], str))
# print(filter_list([35, True, 'abc', 10], bool))

"""
Встроенная функция filter
"""
# def filter_list(list_to_filter, value_type):
#     return list(filter(lambda elem: type(elem) is value_type, list_to_filter))
#
#
# res = filter_list([1, 10, 'abc', True, 5.5], int)
# print(res)

"""
Цикл while
"""
# i = 10
#
# while i < 50:
#     print(i)
#     i += 10

"""
Used 'break' for finish while
"""

# while True:
#     answer = input("Enter yes or no:")
#     if answer == 'no':
#         break

# import random
#
# random_num = random.randint(1, 5)
#
# while True:
#     num = int(input("Guess the number from 1 to 5:"))
#     if num != random_num:
#         print("Try again...")
#         continue
#     print("Congratulation!", random_num)
#     break

# while True:
#     try:
#         num_one = int(input("Enter num one: "))
#         num_two = int(input("Enter num two: "))
#     except ValueError as e:
#         print(e)
#         print("You must enter numbers!")
#         continue
#
#     print(float(num_one / num_two))
#
#     answer = input("Continue? yes or no: ")
#     if answer == 'no':
#         break

"""
Сокращенный цикл for in
"""

# all_nums = [-3, 1, 0, 10, -20, 5]
#
# absolute_nums = []
#
# for num in all_nums:
#     absolute_nums.append(abs(num))
#
# print(absolute_nums) # [3, 1, 0, 10, 20, 5]
#
# print(all_nums) # [-3, 1, 0, 10, -20, 5]

"""
Пример 1
"""
# all_nums = [-3, 1, 0, 10, -20, 5]
#
# absolute_nums = [abs(num) for num in all_nums]
#
# print(absolute_nums) # [3, 1, 0, 10, 20, 5]
#
# print(all_nums) # [-3, 1, 0, 10, -20, 5]

"""
Пример 2
"""

# all_nums = [-3, 1, 0, 10, -20, 5]
#
# positive_nums = [num for num in all_nums if num > 0]
#
# print(positive_nums) # [1, 10, 5]
#
# print(all_nums) # [-3, 1, 0, 10, -20, 5]

"""
Сокращенный for in для наборов set
"""

# my_set = {1, 10, 15}
#
# new_set = {val * val for val in my_set}
#
# print(new_set) # {1, 100, 225}
#
# print(my_set) # {1, 10, 15}

"""
Сокращенный for in для словарей
"""

# my_scores = {
#     'a': 10,
#     'b': 7,
#     'c': 14
# }
#
# scores = {k: v * 10 for k, v in my_scores.items()}
#
# print(scores) # {'a': 100, 'b': 70, 'c': 140}
#
# print(my_scores) # {'a': 10, 'b': 7, 'c': 14}

"""
Практика
"""
# my_scores = [10, 7, 14]
#
# # my_scores = {
# #     'a': 10,
# #     'b': 7,
# #     'c': 14
# # }
#
# scores = {index: elem for index, elem in enumerate(my_scores)}
#
# print(scores) # {0: 10, 1: 7, 2: 14}

# my_motorbike = {
#     'brand': 'bmw',
#     'country': 'germany',
#     'owner': 'anton'
# }
#
# bike = {k: v.upper() for k, v in my_motorbike.items()}
#
# print(bike) # {'brand': 'BMW', 'country': 'GERMANY', 'owner': 'ANTON'}

# my_motorbike = ['BMW', 'Germany', 'Anton']
#
# bike = [el for el in my_motorbike if len(el) > 3]
#
# print(bike) # ['Germany', 'Anton']













