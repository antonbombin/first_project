my_dict = {}
while True:
    if len(my_dict) < 3:
        key = input("Please enter key: ")
        value = input("Please enter value: ")

        my_dict[key] = value
    else:
        break


print(my_dict)

