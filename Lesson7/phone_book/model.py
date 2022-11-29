import os.path
import io_file
import ui_input
import ui_output

DB_FILE = 'db.csv'


def check_command(command, command_dict):
    if command.isdigit():
        return bool(command_dict.get(int(command)))
    else:
        return False


def read_contacts():
    result = [[el for el in ui_output.DB_COL.keys()]]
    db_contact = io_file.csv_reader(DB_FILE)
    return result + db_contact[1:]


def write_contacts(list_contact):
    io_file.csv_writer(DB_FILE, list_contact)


def convert_list_to_dict(list_contact):
    result = {}
    result['contacts'] = []
    for i in range(1, len(list_contact)):
        result['contacts'].append({
            'first_name': list_contact[i][0],
            'last_name': list_contact[i][1],
            'patronymic': list_contact[i][2],
            'phone_number': list_contact[i][3]
        })
    return result


def convert_dict_to_list(dict_contact):
    result = [[*dict_contact['contacts'][0].keys()]]
    for p in dict_contact['contacts']:
        result.append([el for el in p.values()])
    return result


def add_contact():
    db_contact = read_contacts()
    result = []
    ui_output.request_input_contact()
    for el in ui_output.DB_COL.values():
        result.append(input(f"{el}: "))
    db_contact.append(result)
    write_contacts(db_contact)


def delete_contact():
    db_contact = read_contacts()
    print_directory_contact()
    while True:
        try:
            i = ui_input.request_id_for_del()
            if i > 0 and i < len(db_contact):
                db_contact.pop(i)
                write_contacts(db_contact)
                break
            elif i == 0:
                break
            else:
                ui_output.reques_correct_id()
        except:
            ui_output.incorrect_input()


def search_contact():
    db_contact = read_contacts()
    print_directory_contact()
    while True:
            finder = ui_input.request_name_for_search()
            count = 0
            if finder != "0":
                search_result = [
                    ["ИД"]+[el for _, el in ui_output.DB_COL.items()]]
                for i in range(len(db_contact)):
                    if finder.upper() == db_contact[i][1].upper():
                        search_result.append([str(i)]+db_contact[i])
                        count += 1
                if not count:
                    ui_output.not_finding(finder)
                else:
                    ui_output.print_search_db(search_result)
                break
            elif finder == "0":
                break


def import_contact():
    ui_output.print_menu(ui_output.MENU_IMPORT)
    command_user = ui_input.input_command()
    while True:
        if check_command(command_user, ui_output.MENU_IMPORT):
            command_exec_import(command_user)
            break
        else:
            ui_output.request_correct_command()


def import_contact_json():
    path_file = ui_input.path_file()
    import_contacts = convert_dict_to_list(io_file.json_reader(path_file))
    db_contact = io_file.csv_reader(DB_FILE)
    exec_import(import_contacts, db_contact)


def import_contact_csv():
    path_file = ui_input.path_file()
    import_contacts = io_file.csv_reader(path_file)
    db_contact = io_file.csv_reader(DB_FILE)
    exec_import(import_contacts, db_contact)


def exec_import(source, final):
    if final[0] == source[0]:
        final += source[1:]
        write_contacts(final)
        ui_output.final_import()
    else:
        ui_output.error_import()


def export_contact():
    ui_output.print_menu(ui_output.MENU_EXPORT)
    command_user = ui_input.input_command()
    while True:
        if check_command(command_user, ui_output.MENU_EXPORT):
            command_exec_export(command_user)
            break
        else:
            ui_output.request_correct_command()


def export_contact_csv():
    io_file.csv_writer(ui_input.path_file(), read_contacts())
    ui_output.final_export()


def export_contact_json():
    io_file.json_writer(ui_input.path_file(),
                        convert_list_to_dict(read_contacts()))
    ui_output.final_export()


def exit_programm():
    exit()


def print_directory_contact():
    db_contact = read_contacts()
    ui_output.print_db(db_contact)


def edit_contact():
    db_contact = read_contacts()
    print_directory_contact()
    while True:
        try:
            i = ui_input.request_id_for_edit()
            if i > 0 and i < len(db_contact):
                result = []
                ui_output.request_input_contact()
                for el in ui_output.DB_COL.values():
                    result.append(input(f"{el}: "))
                db_contact[i] = result
                write_contacts(db_contact)
                break
            elif i == 0:
                break
            else:
                ui_output.reques_correct_id()
        except:
            ui_output.incorrect_input()


def check_file_db():
    db_contact = []
    col = [[el for el in ui_output.DB_COL.keys()]]
    if os.path.isfile(DB_FILE):
        db_contact = read_contacts()
    if (len(db_contact) > 0 and db_contact[0] != col[0]) or db_contact == []:
        write_contacts(col)


ops = {
    "1": print_directory_contact,
    "2": add_contact,
    "3": delete_contact,
    "4": edit_contact,
    "5": search_contact,
    "6": import_contact,
    "7": export_contact,
    "0": exit_programm
}

ops_export = {
    "1": export_contact_csv,
    "2": export_contact_json,
    "0": exit_programm
}

ops_import = {
    "1": import_contact_csv,
    "2": import_contact_json,
    "0": exit_programm
}


def command_exec(user_command):
    ops[user_command]()


def command_exec_export(user_command):
    ops_export[user_command]()


def command_exec_import(user_command):
    ops_import[user_command]()
