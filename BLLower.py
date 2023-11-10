from os.path import getsize as size
import GUI


def check_empty(file):
    if size(file) == 0:
        return False
    else:
        return True


def read_file(file):
    if size(file) == 0:
        return False
    with open(file, "r") as buff:
        buff = buff.read()
        buff = buff.split("\n")
        GUI.info_message("List of books:")
        for i in range(len(buff)):
            print("        ", buff[i])
        return True


def read(file):
    with open(file, "r") as buff:
        buff = buff.read()
        return buff


def write_file(file, new_text):
    with open(file, "a") as buff:
        buff.write(f"\n{new_text}")
    return True


def del_book(file, book):
    with open(file, "r") as buff:
        buff = buff.read()
        buff = buff.split("\n")
        matrix = []
        for i in range(len(buff)):
            matrix.append(buff[i].split(", "))
        lst = []
        for i in range(len(matrix)):
            if matrix[i][0] != book:
                lst.append(", ".join(matrix[i]))
        new_text = '\n'.join(lst)
        with open(file, "w") as buff_2:
            buff_2.write(new_text)


def check_book(file, book):
    with open(file, "r") as buff:
        buff = buff.read()
        buff = buff.split("\n")
        matrix = []
        for i in range(len(buff)):
            matrix.append(buff[i].split(", "))
        count = 0
        for i in range(len(matrix)):
            if matrix[i][0] == book:
                count += 1
        if count > 0:
            return True
        else:
            return False


def search(file, name):
    if size(file) == 0:
        return False
    with open(file, "r") as buff:
        buff = buff.read()
        if buff.lower().find(name.lower()) != -1:
            buff = buff.split('\n')
            for i in range(len(buff)):
                if buff[i].lower().find(name.lower()) != -1:
                    print(f"         {buff[i]}")
            return True
        else:
            print(f"{name} not found in the list of books")
            return False


def sorting(file):
    buff = read(file)
    buff = buff.split("\n")
    GUI.info_message("Choose the sorting method:\n"
                     "             1 - name of book\n"
                     "             2 - autor\n"
                     "             3 - year\n"
                     "             4 - genre\n")
    while True:
        choice = GUI.input_user()
        if choice == "1":
            matrix = []
            for i in range(len(buff)):
                matrix.append(buff[i].split(", "))
            matrix = sorted(matrix, key=lambda name: name[0])
            for i in range(len(matrix)):
                matrix[i] = ", ".join(matrix[i])
            text = "\n".join(matrix)
            with open(file, "w") as buff:
                buff.write(text)
            break

        if choice == "2":
            matrix = []
            for i in range(len(buff)):
                matrix.append(buff[i].split(", "))
            matrix = sorted(matrix, key=lambda autor: autor[1])
            for i in range(len(matrix)):
                matrix[i] = ", ".join(matrix[i])
            text = "\n".join(matrix)
            with open(file, "w") as buff:
                buff.write(text)
            break

        if choice == "3":
            matrix = []
            for i in range(len(buff)):
                matrix.append(buff[i].split(", "))
            matrix = sorted(matrix, key=lambda year: year[2])
            for i in range(len(matrix)):
                matrix[i] = ", ".join(matrix[i])
            text = "\n".join(matrix)
            with open(file, "w") as buff:
                buff.write(text)
            break

        if choice == "4":
            matrix = []
            for i in range(len(buff)):
                matrix.append(buff[i].split(", "))
            matrix = sorted(matrix, key=lambda genre: genre[3])
            for i in range(len(matrix)):
                matrix[i] = ", ".join(matrix[i])
            text = "\n".join(matrix)
            with open(file, "w") as buff:
                buff.write(text)
            break

    GUI.info_message("List sorted!")
    read_file(file)

