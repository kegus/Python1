# 2. Создать текстовый файл не программно

with open("my_file.txt", mode="r") as f:
    file_lines = f.readlines()
    print("Количество строк: ", len(file_lines))
    for i, words in enumerate(file_lines, 1):
        words = words.split()
        print(f"строка {i} Количество слов: {len(words)}")
