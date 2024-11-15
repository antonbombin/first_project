# import turtle
# import keyboard
#
# keyboard.add_hotkey('w', lambda: turtle.forward(10))
# keyboard.add_hotkey('s', lambda: turtle.backward(10))
# keyboard.add_hotkey('a', lambda: turtle.left(90))
# keyboard.add_hotkey('d', lambda: turtle.right(90))
#
# turtle.exitonclick()


# for i in range(1, 10):
#     for j in range(i):
#         print(i, end='')
#     print('')


# n = -5
# print('Отрицательное' if n < 0 else 'положительное')

# print(len('wfwefwef'))

# my_str = 'fewfweqf'
# print(my_str[-1])

# n = 5
# print('Четное' if n % 2 == 0 else 'Нечетное')

# my_str1 = 'efww'
# my_str2 = 'egerge'
#
# print('Первые буквы сопадают' if my_str1[0] == my_str2[0] else 'не совпадают')

# my_str = 'ночь'
# print(my_str[-2] if my_str[-1] == 'ь' else my_str[-1])

# n = 42334
# while n > 10:
#     n //= 10
# print(n)

# def first_digit(n):
#     if n < 10:
#         return n
#     return first_digit(n // 10)
#
# print(first_digit(177454456445))

# n = 648468
# print(n % 10)

# def first_digit(n):
#     if n < 10:
#         return n
#     return first_digit(n // 10)
#
# m = 177454456445
# print(first_digit(m) + (m % 10))

# n = 177454456445
# num_str = str(n)
# print(len(num_str))


# def first_digit(n):
#     if n < 10:
#         return n
#     return first_digit(n // 10)
#
# print('одинаковые' if first_digit(34234234) == first_digit(34234113344) else 'Отличаются')

# num_list = [1, 2, 3, 4, 5, 6]
# print(num_list[:3])

# my_list = 'rsgdvwgvwvg'
# print(my_list[-2] if len(my_list) > 1 else f'в строке один символ, {my_list[0]}')

# my_str = 'wefwef'
# my_list = []
# for i in my_str:
#     my_list.append(i)
# print(my_list)

# my_list = [1, 2, 3, 4, 5, 6]
# print(my_list[2:5])

# my_dict = {
#     'years': '2025',
#     'month': '12',
#     'day': '31'
# }
# print(f'{my_dict['years']}-{my_dict['month']}-{my_dict['day']}')

# [print(i, end=' ') for i in range(1, 101)]
# print(*range(1, 101))
# print(' '.join(map(str, range(1, 101))))
# n = 100
# while n >= 1:
#     print(n)
#     n -= 1

# my_list = [i for i in range(1, 101)]
# my_list2 = []
# for i in my_list:
#     my_list2.append(my_list[-i])
# print(' '.join(map(str, my_list2)))

# [print(i, end=' ') for i in range(100, 0, -1)]

# [print(i, end=' ') for i in range(2, 101, 2)]

# num = [1, 2, 3, 4, 5, 6]
# print(num[4:])

# my_str = 'fwefwegweaf'
# print(set(my_str))

# def sum_num(n):
#     if n == 1:
#         return 1
#     return n + sum_num(n - 1)
#
# print(sum_num(100))

# num_list = [i for i in range(1, 101)]
# print(sum(num_list))

# def sum_num(n):
#     if n == 2:
#         return 2
#
#     return n + sum_num(n - 2)
#
# print(sum_num(100))

# num_list = [i for i in range(1, 101)]
# count = 0
# for i in num_list:
#     if i % 2 != 0:
#         count += i
# print(count)

# my_list = [1, 2, 3, 4, 5, 6]
# # print(my_list[::2])
# count = 0
# for i in my_list:
#     count += i ** i
#
# print(count)

# my_list = [-1, 2, -3, 4, 5, 11]
# count = 0
# for i in my_list:
#     if i > 0 and i < 10:
#         count += i
#
# print(count)

# my_str = 'abcde'
# reverse_str = my_str[::-1]
# for i in reverse_str:
#     print(i)


# db = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'd': 4,
# }
# count = 0
# for k in db.values():
#     count += k
# print(count)

# db = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'd': 4,
# }
# count = 0
# for v in db.values():
#     count += v ** 2
# print(count)

# my_str = 'abcde'
# my_list = []
# for i in my_str:
#     my_list.append(i)
# print(my_list)

# num = 12345
# my_str = str(num)
# my_list = []
# for i in my_str:
#     my_list.append(int(i))
# print(my_list)

# num = 12345
# num_str = str(num)
# revers_str = num_str[::-1]
# n = int(revers_str)
# print(n)

# num = 12345
# count = 0
# while num > 0:
#     count += num % 10
#     num //= 10
# print(count)



