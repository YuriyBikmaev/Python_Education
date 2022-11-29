DB_COL = {
    "first_name": "ФАМИЛИЯ",
    "last_name": "ИМЯ",
    "patronymic": "ОТЧЕСТВО",
    "phone_number": "ТЕЛЕФОН"
}

MENU = {
    1: "Вывод контактов",
    2: "Добавление контакта",
    3: "Удаление контакта",
    4: "Изменений контакта",
    5: "Фильтр контактов по имени",
    6: "Импорт справочника",
    7: "Экспорт справочника",
    0: "Выход"
}

MENU_EXPORT = {
    1: "Экспорт спраовчника в csv",
    2: "Экспорт справочника в json",
    0: "Выход"
}

MENU_IMPORT = {
    1: "Импорт спраовчника в csv",
    2: "Импорт справочника в json",
    0: "Выход"
}


def print_menu(menu):
    print()
    for i, el in menu.items():
        print(f"{i}. {el}")


def print_db(data):
    for i in range(len(data)):
        if i == 0:
            print("{: >4}".format("ИД"), end="")
            print(" {: >15} {: >15} {: >20} {: >15}".format(
                *[el for _, el in DB_COL.items()]))
        else:
            print("{: >4}".format(i), end="")
            print(" {: >15} {: >15} {: >20} {: >15}".format(*data[i]))


def print_search_db(data):
    for row in data:
        print("{: >4} {: >15} {: >15} {: >20} {: >15}".format(*row))


def request_correct_command():
    print("Введите корректную команду")


def reques_correct_id():
    print("Введите корректное значение ИД из таблицы")


def incorrect_input():
    print("Некорретный ввод!")


def final_export():
    print("Экспорт завершен")


def final_import():
    print("Импорт завершен")


def error_import():
    print("Файл не подходит. Импорт невозможен!")


def not_finding(name):
    print(f"Контакт c именем {name} не найден")


def request_input_contact():
    print("Заполните данные контакта")
