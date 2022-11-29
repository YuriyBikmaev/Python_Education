import sqlite3


departments = {"id": "ИД", "name": "НАИМЕНОВАНИЕ ОТДЕЛА"}

staff = {"id": "ИД", "fio": "ФИО", "salary": "ЗАРПЛАТА", "id_department": "ИД ОТДЕЛА"}


def init_programm():
    connect_staff_db()
    create_staff_db()
    create_departments_db()
    close_connection_db()


def connect_departments_db():
    global DEPARTMENTS_DB
    DEPARTMENTS_DB = sqlite3.connect(r'depatments.db')

def connect_staff_db():
    global STAFF_DB
    STAFF_DB = sqlite3.connect(r'staff.db')

def create_staff_db():
    connect_staff_db()
    cur = STAFF_DB.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS staff(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fio TEXT,
        salary INT,
        id_departments INT
    ); 
    """)
    STAFF_DB.commit()
    cur.close()

def select_departments():
    connect_departments_db()
    cur = DEPARTMENTS_DB.cursor()
    cur.execute("""SELECT * from departments;""")
    result = cur.fetchall()
    cur.close()
    DEPARTMENTS_DB.close()
    return result

def select_staff():
    connect_staff_db()
    cur = STAFF_DB.cursor()
    cur.execute("""SELECT * from staff;""")
    result = cur.fetchall()
    cur.close()
    STAFF_DB.close()
    return result

def create_departments_db():
    connect_departments_db()
    cur = DEPARTMENTS_DB.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS departments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    ); 
    """)
    DEPARTMENTS_DB.commit()
    cur.close()
    

def close_connection_db():
    STAFF_DB.close()
    DEPARTMENTS_DB.close()


def init_programm():
    create_staff_db()
    create_departments_db()


def add_department(name):
    connect_departments_db()
    cur = DEPARTMENTS_DB.cursor()
    cur.execute("INSERT INTO departments(name) VALUES(?);", tuple(name))
    DEPARTMENTS_DB.commit()
    cur.close()
    DEPARTMENTS_DB.close()


def add_staff(list_staff):
    connect_staff_db()
    cur = STAFF_DB.cursor()
    cur.execute("INSERT INTO staff(fio, salary, id_departments) VALUES(?, ?, ?);", tuple(list_staff))
    STAFF_DB.commit()
    cur.close()
    STAFF_DB.close()


def del_staff(data):
    connect_staff_db()
    cur = STAFF_DB.cursor()
    cur.execute("DELETE FROM staff WHERE id = ?;", tuple([data]))
    STAFF_DB.commit()
    cur.close()
    STAFF_DB.close()

def change_departments_in_staff(data):
    connect_staff_db()
    cur = STAFF_DB.cursor()
    cur.execute("UPDATE staff set id_departments = ? WHERE id = ?;", tuple(data[::-1]))
    STAFF_DB.commit()
    cur.close()
    STAFF_DB.close()
