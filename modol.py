import GUI
import BLUpper
import BLLower


def create_text(file):
    while True:
        GUI.info_message("Enter the following information:")
        a = GUI.input_user_str("Enter the name of the book (e.g. The Green Mile) >> ")
        b = GUI.input_user_str("Enter the author of the book (e.g. Stephen King) >> ")
        c = GUI.input_user_str("Enter the year of publication of the book (e.g. 1996) >> ")
        while True:
            if c.isdigit():
                break
            else:
                GUI.error_message("You have entered the letters! Enter the number.")
                c = GUI.input_user_str("Enter the year of publication of the book (e.g. 1996) >> ")
        d = GUI.input_user_str("Enter the genre of the book (e.g. novel) >> ")
        lst = [a, b, c, d]
        book = ', '.join(lst)
        catalog = BLLower.read(file)
        if catalog.lower().find(book.lower()) == -1:
            BLLower.write_file(file, book)
            GUI.info_message("The book has been added successfully!")
            return True
        else:
            GUI.error_message("Such a book already exists!")
            while True:
                buff = GUI.input_user_str("Do you want to add another book? Enter yes or no >> ")
                if buff == "no":
                    return
                elif buff == "yes":
                    break


def parsing_file(file):
    GUI.command_list()
    while True:
        command = GUI.input_user()
        if command == "stop":
            return command
        elif command == "change":
            GUI.info_message("Back to the file selection...")
            break
        elif command == "info":
            GUI.command_list()
        else:
            check = BLUpper.check_command(command, file)
            if check:
                GUI.info_message("Select the following action")
            else:
                GUI.error_message("No such command was found. Enter 'info' to output the available commands")


def open_file():
    while True:
        file_name = GUI.input_name_file()
        if BLUpper.check_exist(file_name):
            return file_name
        elif file_name == "stop":
            return file_name
        else:
            if not_found_file(file_name) == "stop":
                file_name = "stop"
                return file_name


def not_found_file(file_name):
    GUI.error_message("File not found. Create it? (yes/no)")
    while True:
        command = GUI.input_user()
        if command == "yes":
            BLUpper.create_file(file_name)
            GUI.info_message("File was created successfully! Enter the file name to open it.")
            return command
        elif command == "no":
            GUI.info_message("Choose a file by entering its name")
            return command
        elif command == "stop":
            return command
        else:
            GUI.error_message("Command input error. Available yes or no")


def run():
    while True:
        file = open_file()
        if file == "stop":
            return
        if parsing_file(file) == "stop":
            return
