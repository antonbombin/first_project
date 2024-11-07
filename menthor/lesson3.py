"""
Задание:
Реализовать БД товаров (БД будет в виде обычного списка),
с возможностью посмотреть, добавить, удалить, изменить товар (для хранения использовать список)
"""

product = ['Milk', 'Chocolate', 'Chips']
while True:
    decease = input('Что вы хотите сделать? ')
    if decease == 'посмотреть':
        for el in enumerate(product, 1):
            print(el[0], el[1])
    if decease == 'добавить':
        add_new = input('Что вы хотите добавить? ')
        product.append(add_new)
        print(product)
    if decease == 'удалить':
        del_el = input('Какой элемент вы хотели бы удалить? ')
        for el in product:
            if el == del_el:
                product.remove(del_el)
                print(product)
    if decease == 'изменить':
        edit_el = input('Какой элемент вы хотели бы изменить? ')
        for el in product:
            if el == edit_el:
                new_el = input('Какой новый элемент вы хотите добавить? ')
                for i in enumerate(product):
                    if i[1] == el:
                        product.remove(el)
                        product.insert(i[0], new_el)
                print(product)
    if decease == 'q':
        print('Работа с БД завершена!')
        break




