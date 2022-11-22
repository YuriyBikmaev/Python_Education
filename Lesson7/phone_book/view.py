DB_COL = {
    "id": "ИД", 
    "first_name": "ФАМИЛИЯ", 
    "last_name": "ИМЯ", 
    "patronymic": "ОТЧЕСТВО", 
    "phone_number": "ТЕЛЕФОН"
    }

MENU = {
    "1": "Вывод контактов",
    "2": "Добавление контакта",
    "3": "Удаление контакта",
    "4": "Изменений контакта",
    "5": "Фильтр контактов по имени",
    "6": "Импорт справочника",
    "7": "Экспорт справочника",
    "0": "Выход"
}

def print_menu():
    for i, el in MENU.items():
        print(f"{i}. {el}")


def print_row_db(row):
    result = ''
    for col in list(row):
        result += col + " ".rjust(10)
    print(result)


def print_db(data):
    for row in data:
        print("{: >4} {: >15} {: >15} {: >15} {: >15} {: >15}".format(*row))


def input_contact(contact_header):
    ...

def input_command():
    return input('Введите номер действия: ')