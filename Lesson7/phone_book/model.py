import os.path
import view
import io_file

DB_FILE = 'db.csv'


def check_command(command, command_dict):
    if command.isdigit():
        return bool(command_dict.get(int(command)))
    else:
        return False


def read_contacts():
    result = [[el for el in view.DB_COL.keys()]]
    db_contact = io_file.csv_reader(DB_FILE)
    return result + db_contact[1:]


def write_contacts(list_contact):
    io_file.csv_writer(DB_FILE, list_contact)


def add_contact():
    db_contact = read_contacts()
    result = []
    view.input_contact()
    for el in view.DB_COL.values():
        result.append(input(f"{el}: "))
    db_contact.append(result)
    write_contacts(db_contact)


def delete_contact():
    db_contact = read_contacts()
    print_directory_contact()
    while True:
        try:
            i = int(input("Введите ИД удаляемого контакта  (для отмены введите 0): "))
            if i > 0 and i < len(db_contact):
                db_contact.pop(i)
                write_contacts(db_contact)
                break
            elif i == 0:
                break
            else:
                print("Введите корректное значение ИД из таблицы")
        except:
            print("Некорретный ввод!")


def search_contact():
    db_contact = read_contacts()
    print_directory_contact()
    while True:
        try:
            finder = input("Введите Имя контакта  (для отмены введите 0): ")
            count = 0
            if finder != "0":
                search_result = [["ИД"]+[el for _, el in view.DB_COL.items()]]
                for i in range(len(db_contact)):
                    if finder.upper() == db_contact[i][1].upper():
                        search_result.append([str(i)]+db_contact[i])
                        count += 1
                if not count:
                    print(f"Контакт c именем {finder} не найден")
                else:
                    view.print_search_db(search_result)
                break
            elif finder == "0":
                break
        except:
            print("Некорретный ввод!")


def import_contact():
    path_file = input("Введите путь к файлу: ")
    import_contacts = io_file.csv_reader(path_file)
    db_contact = io_file.csv_reader(DB_FILE)
    if db_contact[0] == import_contacts[0]:
        db_contact += import_contacts[1:]
        write_contacts(db_contact)
        print("Импорт контактов успешно завершен")
    else:
        print("Файл не подходит. Импорт невозможен!")


def export_contact():
    db_contact = read_contacts()
    path_file = input("Введите путь к файлу: ")
    io_file.csv_writer(path_file, db_contact)
    print("Экспорт завершен")


def exit_programm():
    exit()


def print_directory_contact():
    db_contact = read_contacts()
    view.print_db(db_contact)


def edit_contact():
    db_contact = read_contacts()
    print_directory_contact()
    while True:
        try:
            i = int(input("Введите ИД изменяемого контакта (для отмены введите 0): "))
            if i > 0 and i < len(db_contact):
                result = []
                view.input_contact()
                for el in view.DB_COL.values():
                    result.append(input(f"{el}: "))
                db_contact[i] = result
                write_contacts(db_contact)
                break
            elif i == 0:
                break
            else:
                print("Введите корректное значение ИД из таблицы")
        except:
            print("Некорретный ввод!")



def check_file_db():
    db_contact = []
    col = [[el for el in view.DB_COL.keys()]]
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


def command_exec(user_command):
    ops[user_command]()
