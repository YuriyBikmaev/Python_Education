import ui.ui_view as view
import models

MENU_ACTIONS = {
    1: ["Вывести список отделов", models.get_departments, view.show_departments],
    2: ["Вывести список всех сотрудников", models.get_staff, view.show_staff],
    3: ["Вывести список всех сотрудников c наименованиями отделов", models.get_staff_with_department, view.show_staff],
    4: ["Вывести список сотрудников отдела", view.show_staff_in_departments],
    5: ["Добавить отдел", view.input_department, models.add_department],
    6: ["Добавить сотрудника", view.input_staff, models.add_staff],
    7: ["Перевести сотрудника в другой отдел", view.input_new_department_in_staff, models.change_departments_in_staff],
    8: ["Удалить сотрудника", view.input_id_staff, models.del_staff],
    9: ["Экспорт сотрудников с наименованиями отделов в csv", view.input_path_file, models.export_contact_csv],
    0: ["Выйти из программы", exit]
}


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
