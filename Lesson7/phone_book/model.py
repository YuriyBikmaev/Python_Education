import csv, os.path, view

DB_PHONE = 'db.csv'
DB_CONTACT = []

def check_command_user(command, COMMAND_LIST):
    if command.isdigit():
        return bool(COMMAND_LIST.get(int(command)))
    else:
        return False

def init_programm():
    global DB_CONTACT
    DB_CONTACT = csv_reader(DB_PHONE)

def add_contact():
    ...

def delete_contact():
    ...

def search_contact():
    ...

def import__directory_contact():
    ...

def export__directory_contact():
    ...

def exit_programm():
    ...

def print_directory_contact():
    view.print_db(DB_CONTACT)  

def edit_contact():
    ...

def csv_writer(file_name, list_writing):
    with open(file_name, encoding="utf-8") as w_file:
        file_writer = csv.writer(w_file, delimiter=";")
        file_writer.writerow(list_writing)


def csv_reader(file_name):
    result = []
    with open(file_name, encoding="utf-8") as r_file:
        file_reader = csv.reader(r_file, delimiter=";")
        for row in file_reader:
            result.append(row)
    return result


# def check_file_db(name_file, header_db):
#     if not os.path.isfile(name_file):
#         csv_writer(header_db)
#     else:
#         result = csv_reader()
#         if result[0] != header_db:
#             csv_writer(header_db)

def input_command():
    ...

ops = {
    "1": print_directory_contact,
    "2": add_contact,
    "3": delete_contact,
    "4": edit_contact,
    "5": search_contact,
    "6": import__directory_contact,
    "7": export__directory_contact,
    "0": exit_programm
}

def command_exec(user_command):
    ops[user_command]()
