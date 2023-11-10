red = "\033[31m"
green = "\033[92m"
purple = "\033[35m"
reset = "\033[0m"


def info():
    return f"{green}  INFO: {reset}"


def error():
    return f"{red} ERROR: {reset}"


def you():
    return f"{purple}   YOU: {reset}"


def ending():
    print(f"{info()} The program is ending...")
    input("         Press Enter for exit")


def starting_message():
    print(f"{info()} The program is starting...")


def input_name_file():
    file = input(f"{you()} Choose a book catalog >> ")
    return file


def error_message(text):
    print(f"{error()} {text}")


def input_user():
    file = input(f"{you()} >> ")
    return file


def input_user_str(text):
    file = input(f"{you()} {text} ")
    return file


def info_message(text):
    print(f"{info()} {text}")


def command_list():
    print(f"{info()} List of available commands:\n"
          f"             write - adding a book\n"
          f"             read - reading a catalog\n"
          f"             search - search a book\n"
          f"             del - deleting a book\n"
          f"             change - change the book catalog\n"
          f"             stop - exiting the program\n"
          f"             sort - sort the catalog by attributes\n")
