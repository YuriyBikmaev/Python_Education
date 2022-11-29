import model
import ui_output
import ui_input


def run():
    model.check_file_db()
    while True:
        if ui_input.waiting_main_command() == "1":
            ui_output.print_menu(ui_output.MENU)
            command_user = ui_input.input_command()
            if model.check_command(command_user, ui_output.MENU):
                model.command_exec(command_user)
            else:
                print("Введите корректную команду")
        else:
            exit()
