import model, view


def run():
    play = True
    while play:
        command_list = view.print_menu()
        model.init_programm()
        model.command_exec(view.input_command())
        play = False
        # 
        # view.print_db(data)
        # model.check_file_db(DB_PHONE, list(DB_COL))
        # view.print_row_db(DB_COL)

