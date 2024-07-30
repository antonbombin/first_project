my_list = [10, 11, 20, 30, 55, 60]
# Показать четные элементы на нечетных позициях

for i in range(0, len(my_list), 2):
    if my_list[i] % 2 == 0:
        print(my_list[i], end=' ')



