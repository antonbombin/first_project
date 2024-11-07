"""
task 1 lesson 34
"""
# with open("text.txt", 'r', encoding="utf-8") as file:
#     text = file.read().strip().split()
#     count = ''
#     for i in text:
#         if len(i) > len(count):
#             count = i
#     print(count)
#     max_word_len = max(len(i) for i in text)
#     longest_words = [i for i in text if len(i) == max_word_len]
#     print(longest_words)


# def longest_words(file):
#     with open(file, encoding='utf-8') as text:
#         words = text.read().split()
#         max_length = len(max(words, key=len))
#         sought_words = [word for word in words if len(word) == max_length]
#         if len(sought_words) == 1:
#             return sought_words[0]
#         return sought_words
#
#
# print(longest_words('text.txt'))

"""
task 2 lesson 34
"""

# with open("text.txt", 'r', encoding="utf-8") as file:
#     words = file.read().strip().split()
#     lines = -1
#     while lines < 0:
#         lines = int(input("Введите количество выводимых строк: "))
#         if lines > 0:
#             for word in words[:lines]:
#                 print(word)
#         else:
#             print("Вы ввели отрицательное число")

"""
lesson 35
"""
# dict_words = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11,
#               'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
#               's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
#
# with open("stats_of_english.txt", 'r', encoding='utf-8') as file:
#     text = file.read().strip().lower()
#     count = 0
#     length_letter = []
#     res_list = []
#     for word in text:
#         res_list.append(sum(dict_words[i] for i in dict_words if i in dict_words))
#     print(res_list)
#         for letter in word.lower():
#             if letter in dict_words:
#                length_letter.append(dict_words[letter])
#         res_list.append(sum(length_letter))
#
    # def word_score(word):
    #     return sum(ord(char) - ord('a') + 1 for char in word)
    #
    #
    # def highest_scoring_word(sentence):
    #     words = sentence.split()
    #     highest_word = ""
    #     highest_score = 0
    #
    #     for word in words:
    #         score = word_score(word)
    #         if score > highest_score:
    #             highest_score = score
    #             highest_word = word
    #     return highest_word
    #
    #
    # result = highest_scoring_word(text)
    # print(result)


"""
lesson 36 task 1
"""
#
# vowels_letter = 'aeuio'
# with open("stats_of_english.txt", 'r', encoding="utf-8") as file:
#     words = file.read().strip().split()
#     count = 0
#     for word in words:
#         for letter in word:
#             if letter in vowels_letter:
#                 count += 1
#     print(count)

"""
lesson 36 task 2
"""
# with open("a.txt") as file:
#     count = 0
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     for i in file.read():
#         if i in numbers:
#             count += 1
#     print(count)

"""
lesson 36 task 3 
"""
# with open("a.txt") as file:
#     num_letters = {}
#     for i in file.read().lower():
#         if not i.isalpha():
#             continue
#         if i not in num_letters:
#             num_letters[i] = 0
#         num_letters[i] += 1
#     for k, v in num_letters.items():
#         print(f'Буква {k} встречается в тексте {v} раз!')

"""
lesson 37 task 1
"""
# with open("symbol.txt", 'r', encoding="utf-8") as file:
#     symbol = file.read().strip()
#     symbol_dict = {}
#     for i in symbol:
#         if i.isalpha() or i == '\n':
#             continue
#         if i not in symbol_dict:
#             symbol_dict[i] = 0
#         symbol_dict[i] += 1
#     for k, v in symbol_dict.items():
#         print(f'Символ {k} встречается в наборе {v} раз!')


# import string
#
#
# def count_special_symbol(file_path):
#     special_sym_count = {}
#     special_symbols = string.punctuation
#
#     with open(file_path, 'r', encoding='utf-8') as file:
#         text = file.read().strip()
#         for i in text:
#             if i not in special_symbols:
#                 continue
#             if i not in special_sym_count:
#                 special_sym_count[i] = 0
#             special_sym_count[i] += 1
#         for k, v in special_sym_count.items():
#             print(f'Символ {k} встречается в наборе {v} раз!')
#
#
# count_special_symbol("symbol.txt")

"""
lesson 37 task 2
"""
# with open("num.txt", 'r', encoding="utf-8") as file:
#     text = file.read().strip().split()
#     list_text = [int(i) for i in text]
    # differences = []
    # for i in range(len(list_text) - 1):
    #     difference = list_text[i] - list_text[i + 1]
    #     differences.append(difference)
    # print(differences)
    # count = list_text[0]
    # for i in range(len(list_text) - 1):
    #     count -= list_text[i + 1]
    # print(count)

"""
lesson 37 task 3
"""

# with open("math.txt", 'r', encoding="utf-8") as file:
#     text = file.read().strip().split()
#     start = float(text[0])
#     for i in range(1, len(text) - 1, 2):
#         operator = text[i]
#         next_num = float(text[i + 1])
#         if operator == '+':
#             start += next_num
#         elif operator == '-':
#             start -= next_num
#         elif operator == '*':
#             start *= next_num
#         elif operator == '/':
#             start /= next_num
#         else:
#             print("Некорректный оператор вычисления")
#
#     print(start)









