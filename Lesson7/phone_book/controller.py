import model, view


def run():
    model.check_file_db()
    while True:
        if view.waiting_command()=="1":
            view.print_menu()
            command_user = view.input_command()
            if model.check_command(command_user, view.MENU):
                model.command_exec(command_user)
            else:
                print("Введите корректную команду")
        else:
            exit()
        
        # 
        # view.print_db(data)
        # model.check_file_db(DB_PHONE, list(DB_COL))
        # view.print_row_db(DB_COL)

