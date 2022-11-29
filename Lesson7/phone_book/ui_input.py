def path_file():
    return input("Введите путь к файлу: ")


def request_id_for_edit():
    return int(input("Введите ИД изменяемого контакта (для отмены введите 0): "))


def request_id_for_del():
    return int(input("Введите ИД удаляемого контакта (для отмены введите 0): "))


def request_name_for_search():
    return input("Введите Имя контакта  (для отмены введите 0): ")


def input_command():
    return input('Введите номер действия: ')

def waiting_main_command():
    print("\nВыберите действие:")
    print("1. Вывести меню")
    print("0. Выход из программы")
    return input('Ожидание ввода команды: ')
