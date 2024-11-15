def read_users() -> dict:
    """
    Создаем словарь из файла с содержанием (логин: пароль)

    В функции создаем пустой словарь в него построчно записываем данные из файла. В конце функции возвращаем заполненный
    словарь.
    """
    users = {}
    try:
        with open("users.txt", 'r', encoding='utf-8') as file:
            for line in file:
                login, password = line.strip().split(':')
                users[login] = password
    except FileNotFoundError as e:
        print(e)
    return users


def new_user(login: str, password: str) -> None:
    """
    Записываем в файл нового пользователя.

    В функцию передаем логин и пароль, внутри функции записываем новые данные в формате словаря
    Args:
        login: str - логин введеный пользователем при регистрации
        password: str - пароль введенный пользователем при регистрации
    """
    try:
        with open("users.txt", "a", encoding="utf-8") as file:
            file.write(f"{login}:{password}\n")
    except FileNotFoundError as e:
        print(e)


def authorization_user() -> None:
    """
    Авторизация пользователя

    В функции пользователь вводит логин и пароль, далее мы проверяем есть ли данный логин и пароль в файле с
    пользователями, в результате выводим либо успешно, либо неуспешно
    """
    login = input("Введите ваш логин: ")
    password = input("Введите ваш пароль: ")
    users = read_users()

    if login in users and users[login] == str(password):
        print("Авторизация прошла успешно")
    else:
        print("Введен неверный логин и пароль")


def registration_user() -> None:
    """
    Регистрация нового пользователя

    В функции пользователь вводит логин и пароль, осуществляем проверку на корректность введенных данных в соответствии
    с требованиями и выводим результат - либо регистрация прошла успешно, либо информацию о наличии данного пользователя
    в файле
    """
    while True:
        login = input("Придумайте логин: ")
        if len(login) < 3 or len(login) > 20:
            print("Ваш логин должен быть больше 3 символов и меньше 20, Введите повторно")
        else:
            break
    while True:
        password = input("Придумайте пароль: ")
        if len(password) < 4 or len(password) > 32:
            print("Пароль должен быть больше 4 символов и меньше 32, Введите повторно")
        else:
            break
    users = read_users()
    if login in users:
        print("Логин уже существует")
    else:
        new_user(login, password)
        print("Регистрация прошла успешно")


def choose_action() -> None:
    """
    Выбрать регистрацию или авторизацию

    В функции пользователь выбирает, что он хочет либо пройти регистрации, либо авторизацию, либо выйти. Исходя из
    выбора пользователя осуществляем переход к определенной функции
    """
    while True:
        request = input("Вы хотели бы авторизоваться или зарегистрироваться? Введите а или р"
                        " или выход (для завершения работы!) - ")
        if request == 'р':
            registration_user()
        elif request == 'a':
            authorization_user()
        elif request == 'выход':
            break
        else:
            print('Введите корректную команду для работы авторизации или регистрации')


choose_action()
