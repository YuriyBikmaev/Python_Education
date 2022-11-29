import ui.ui_view as view
import models

def run():
    models.init_programm()
    menu_number = True
    while menu_number:
        menu_number = view.menu()
        if menu_number in MENU_ACTIONS.keys():
            input_data = MENU_ACTIONS[menu_number][1]()
            if input_data:
                MENU_ACTIONS[menu_number][2](input_data)
        else:
            view.incorrect_input()


MENU_ACTIONS = {
    1: ["Вывести список отделов", models.select_departments, view.show_departments],
    2: ["Вывести список всех сотрудников", models.select_staff, view.show_staff],
    3: ["Вывести список сотрудников отдела", view.show_staff_in_departments],
    4: ["Добавить отдел", view.input_department, models.add_department],
    5: ["Добавить сотрудника", view.input_staff, models.add_staff],
    6: ["Перевести сотрудника в другой отдел", view.input_new_department_in_staff, models.change_departments_in_staff],
    7: ["Удалить сотрудника", view.input_id_staff, models.del_staff],
    8: ["Экспорт сотрудников с наименованиями отделов в csv", ...],
    0: ["Выйти из программы", exit]
}