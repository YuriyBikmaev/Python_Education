MENU_ITEMS = [
    "Выход",
    "a + b",
    "a - b",
    "a * b",
    "a / b",
]

def menu():
    for index, item in enumerate(MENU_ITEMS):
        print(f"{index}. {item}")

