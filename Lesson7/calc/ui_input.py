from ui_view import MENU_ITEMS

def menu_input():
    """
    Функция получает от пользователя выбранный пункт меню
    :return: число, пункт меню
    """
    # result = int(input("Выберите пункт меню: "))
    return int(input("Выберите пункт меню: "))

    
def input_char(ch):
    print(f"Введите {ch}: ", end="")

def check_menu_item(menu_item):
    """
    Функция проверяет корректность выбранного пункта меню
    :return: логическое значение
    """
    if 0 <= menu_item < len(MENU_ITEMS):
        return False
    return True
