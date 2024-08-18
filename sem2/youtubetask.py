n = input("Vvedite chislo: ")
while n != 'q':
    if int(n) % 2 == 0:
        print("Chislo chetnoe")
        n = input("Vvedite chislo: ")
    else:
        print("Chislo nechetnoe")
        n = input("Vvedite chislo: ")


