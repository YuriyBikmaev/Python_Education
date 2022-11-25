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


def print_menu():
    print()
    for i, el in MENU.items():
        print(f"{i}. {el}")


def print_db(data):
    for i in range(len(data)):
        if i==0:
            print("{: >4}".format("ИД"), end="")
            print(" {: >15} {: >15} {: >20} {: >15}".format(*[el for _, el in DB_COL.items()]))
        else:
            print("{: >4}".format(i), end="")
            print(" {: >15} {: >15} {: >20} {: >15}".format(*data[i]))

def print_search_db(data):
    for row in data:
            print("{: >4} {: >15} {: >15} {: >20} {: >15}".format(*row))


def input_contact():
    print("Заполните данные контакта")

def input_command():
    return input('Введите номер действия: ')

def waiting_command():
    print("\nВыберите действие:")
    print("1. Вывести меню")
    print("0. Выход из программы")
    return input('Ожидание ввода команды: ')