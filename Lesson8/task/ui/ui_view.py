import models
import ui.ui_controller as controller


def menu():
    print()
    for key, item in controller.MENU_ACTIONS.items():
        print(key, item[0])
    print()
    while True:
        result = input("Выберите пункт меню: ")
        if result.isdigit():
            return int(result)

def incorrect_input():
    print("Введите корректное значение")

def show_departments(data):
    print_row_departments(models.departments.values())
    for el in data:
        print_row_departments(el)


def print_row_departments(row):
    print("{: >5} {: >25}".format(*row))


def show_staff(data):
    print_row_staff(models.staff.values())
    for el in data:
        print_row_staff(el)


def print_row_staff(row):
    print("{: >5} {: >30} {: >12} {: >12}".format(*row))


def input_department():
    return [input("Название отдела: ")]


def input_staff():
    result = [input(f"Введите {el}: ")
              for el in models.staff.values() if el != 'ИД']
    return result


def input_id_department():
    while True:
        result = input("Введите id отдела: ")
        if result.isdigit():
            return int(result)
        else:
            incorrect_input()


def input_id_staff():
    return int(input("Введите id сотрудника: "))


def show_staff_in_departments():
        id_department = input_id_department()
        show_staff(select_staff_in_department(id_department))

    # for el in models.staff:
    #     if el['id_accounting'] == id_department:
    #         print_row_staff(el.values())

def select_staff_in_department(id_department):
    models.connect_staff_db()
    cur = models.STAFF_DB.cursor()
    cur.execute(f"""SELECT * from staff WHERE id_departments = {id_department};""")
    result = cur.fetchall()
    cur.close()
    models.STAFF_DB.close()
    return result


def input_new_department_in_staff():
    return [input_id_staff(), input_id_department()]
