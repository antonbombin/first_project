"""
Будем говорить, что число a лучше числа b, если сумма цифр a больше суммы цифр числа b, а в случае равенства сумм их цифр, если число a меньше числа b.
Например, число 124 лучше числа 123, так как у первого из них сумма цифр равна семи, а у второго – шести.
Также, число 3 лучше числа 111, так как у них равны суммы цифр, но первое из них меньше.
Дано число n. Найдите такой его делитель (само число n и единица считаются делителями числа n), который лучше любого другого делителя числа n.
"""
# import time
# n = int(input("Введите число n: "))
# time_start = time.time()
# divider = []
# for i in range(1, n + 1):
#     if n % i == 0:
#         divider.append(i)
#
# count = 0
# print(divider)
# best_dividers = []
# for i in divider:
#     if i // 10 != 0:
#         # while i > 1:
#         #     count += (i % 10)
#         #     i = i // 10
#         # best_dividers.append(count)
#         best_dividers.append(sum(int(digit) for digit in str(i)))
#     else:
#         best_dividers.append(i)
# # print(best_dividers)
# # print(max(best_dividers))
# print(divider[best_dividers.index(max(best_dividers))])
# time_finish = time.time()
# print(time_finish - time_start)


