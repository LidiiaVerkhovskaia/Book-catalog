from os.path import exists
import BLLower
import GUI
import modol


def check_exist(name):
    if exists(name):
        return True
    else:
        return False


def create_file(name):
    with open(name, "w") as file:
        pass


def check_command(buff, file):
    if buff == "read":
        if BLLower.read_file(file):
            return True
        else:
            GUI.error_message("File is empty!")
            return True
    elif buff == "write":
        modol.create_text(file)
        return True
    elif buff == "del":
        if BLLower.check_empty(file):
            while True:
                book = GUI.input_user_str("Enter the name of the book you want to delete. 'stop' for cancel. >> ")
                if book != "stop" and book != '':
                    if BLLower.check_book(file, book):
                        buff = GUI.input_user_str("Do you really want to delete this book? Enter yes or no >> ")
                        if buff == "yes":
                            BLLower.del_book(file, book)
                            GUI.info_message("The book was deleted successfully!")
                            break
                        elif buff == "no":
                            break
                        else:
                            GUI.error_message("Command input error! Available yes or no")
                    else:
                        GUI.info_message("The book not found!")
                elif book == 'stop':
                    GUI.info_message("Deleting a book has been canceled")
                    break
            return True
        else:
            GUI.error_message("Deletion is not possible. File is empty!")
            return True
    elif buff == "search":
        GUI.info_message("Enter the attribute of the book you want to find.")
        name = GUI.input_user()
        if BLLower.search(file, name):
            return True
        else:
            GUI.info_message("There is no such book in the list. Do you want to add a book?")
            while True:
                buff = GUI.input_user_str("Enter yes or no >> ")
                if buff == "yes":
                    modol.create_text(file)
                    return True
                elif buff == "no":
                    return True
                else:
                    GUI.error_message("Command input error. Available yes or no")
    elif buff == "sort":
        BLLower.sorting(file)
        return True
    else:
        return False

