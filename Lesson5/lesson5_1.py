# 1. Создать программно файл в текстовом формате

with open("my_file.txt", mode="a+") as f:
    read_line = "n"
    while read_line:
        read_line = input("Введите строку: ")
        if read_line:
            read_line += "\n"
            f.write(read_line)
    f.seek(0)
    print(list(map(lambda el: el.replace("\n", ""), f.readlines())))
