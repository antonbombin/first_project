"""
Задание:
• Программа 'придумывает' число в заданной уровнем сложности последовательности
1. Новичок(1) - от 0 до 10;
2. Спортсмен(2) - от 0 до 25;
3. Мастер(3) - от 0 до 50;
4. Зверь(4) - от 0 до 100;
• Пользователь вводит число, программа печатает угадал он или нет
• Программа выполняется до тех пор, пока пользователь не угадает число
• Если пользователь потратил менее 3 попыток, вывести: Удача на твоей стороне! В любом другом случае вывести число потраченных попыток
• Усложнить программу. Добавить подсказку больше угаданное число или меньше, чем 'придуманное' программой
"""
# import random
# level = int(input("Выберите уровень сложности - 1/2/3/4: "))
# count = 0
# if level == 1:
#     num = random.randint(0, 10)
#     while True:
#         num_user = int(input("Введите число, проверим удачу: "))
#         count += 1
#         if num_user == num:
#             if count <= 3:
#                 print("Удача на твоей стороне! ")
#                 break
#             else:
#                 print(f"Ты угадал число с {count} попытки")
#                 break
#         elif num_user > num:
#             print("Загаданное число меньше вашего")
#             continue
#         else:
#             print("Загаданное число больше вашего")
#             continue
#
# elif level == 2:
#     num2 = random.randint(0, 25)
#     while True:
#         num_user2 = int(input("Введите число, проверим удачу: "))
#         count += 1
#         if num_user2 == num2:
#             if count <= 3:
#                 print("Удача на твоей стороне! ")
#                 break
#             else:
#                 print(f"Ты угадал число с {count} попытки")
#                 break
#         elif num_user2 > num2:
#             print("Загаданное число меньше вашего")
#             continue
#         else:
#             print("Загаданное число больше вашего")
#             continue
# elif level == 3:
#     num3 = random.randint(0, 50)
#     while True:
#         num_user3 = int(input("Введите число, проверим удачу: "))
#         count += 1
#         if num_user3 == num3:
#             if count <= 3:
#                 print("Удача на твоей стороне! ")
#                 break
#             else:
#                 print(f"Ты угадал число с {count} попытки")
#                 break
#         elif num_user3 > num3:
#             print("Загаданное число меньше вашего")
#             continue
#         else:
#             print("Загаданное число больше вашего")
#             continue
# else:
#     num4 = random.randint(0, 100)
#     while True:
#         num_user4 = int(input("Введите число, проверим удачу: "))
#         count += 1
#         if num_user4 == num4:
#             if count <= 3:
#                 print("Удача на твоей стороне! ")
#                 break
#             else:
#                 print(f"Ты угадал число с {count} попытки")
#                 break
#         elif num_user4 > num4:
#             print("Загаданное число меньше вашего")
#             continue
#         else:
#             print("Загаданное число больше вашего")
#             continue

"""
lesson 30
"""

"""
Напишите программу, которая будет открывать определенный файл и выводить на печать построчно последние строки в количестве lines
(на всякий случай проверим, что задано положительное целое число).
"""
# lines = int(input("Введите количество строк: "))
#
# with open("new_file.txt", 'r', encoding="utf-8") as file:
#     text = file.read().strip().split("\n")
#     for i in text[-lines:]:
#         print(i)


"""
1. Напишите проверку на то, является ли строка палиндромом. 
Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево. Слова находятся в файле
"""

# with open("new_file.txt", 'r', encoding="utf-8") as file:
#     text = file.read().strip().split()
#     for i in text:
#         new_i = i[::-1]
#         if i == new_i and len(i) > 1:
#             print(i)


