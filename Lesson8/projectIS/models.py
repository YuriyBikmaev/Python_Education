import sqlite3
import io_file
import ui.ui_view as view

DB_PATH = r'db/organization.db'


def init_programm():
    # connect_staff_db()
    # create_staff_db()
    # create_departments_db()
    # close_connection_db()
    create_tables_db()


def connect_organization_db():
    return sqlite3.connect(DB_PATH)


def close_connection_db(db):
    db.close()


def create_tables_db():
    with sqlite3.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.executescript(
            """
            CREATE TABLE IF NOT EXISTS staff
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fio TEXT,
                salary INT,
                departments_id INT
            ); 

            CREATE TABLE IF NOT EXISTS departments
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name TEXT
            );
            """)
        db.commit()
        cur.close()


def get_data_db(sql):
    result = []
    with sqlite3.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.execute(sql)
        result = [tuple([description[0] for description in cur.description])]
        result += cur.fetchall()
        cur.close()
    return result


def change_data_db(sql, data):
    with sqlite3.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.execute(sql, tuple(data))
        cur.close()


def get_departments():
    return get_data_db(
        """
        SELECT id as ИД, name as 'НАИМЕНОВАНИЕ ОТДЕЛА' 
        FROM departments
        ;""")


def get_staff():
    return get_data_db(
        """
        SELECT  id as ИД, 
                fio as ФИО, 
                salary as ЗАРПЛАТА, 
                departments_id as 'ИД ОТДЕЛА' 
        FROM staff
        ;""")


def get_staff_with_department():
    return (get_data_db(
        """
        SELECT  staff.id as ИД,
                staff.fio as ФИО, 
                staff.salary as ЗАРПЛАТА, 
                departments.name as 'НАИМЕНОВАНИЕ ОТДЕЛА' 
        FROM staff 
        LEFT JOIN departments 
        ON staff.departments_id = departments.id
        ;"""))


def get_staff_in_department(id_department):
    return (get_data_db(
        f"""
        SELECT  id as ИД, 
                fio as ФИО, 
                salary as ЗАРПЛАТА, 
                departments_id as 'ИД ОТДЕЛА' 
        FROM staff 
        WHERE departments_id = {id_department}
        ;"""))


def add_department(name):
    change_data_db(
        """
        INSERT INTO departments(name) VALUES(?)
        ;""", name)


def add_staff(list_staff):
    change_data_db(
        """
        INSERT INTO staff(fio, salary, departments_id) 
        VALUES(?, ?, ?)
        ;""", tuple(list_staff))


def del_staff(data):
    change_data_db(
        """
        DELETE FROM staff 
        WHERE id = ?
        ;""", tuple([data]))


def change_departments_in_staff(data):
    change_data_db(
        """UPDATE staff SET departments_id = ? WHERE id = ?;""", tuple(data[::-1]))


def convert_list_for_export_csv():
    source_list = get_staff_with_department()
    result = []
    for row in source_list:
        result.append([*row])
    return result


def export_contact_csv(file_path):
    try:
        io_file.csv_writer(file_path, convert_list_for_export_csv())
        view.print_final_export()
    except:
        view.print_error_export()
